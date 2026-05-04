from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from django.conf import settings

from .forms import LoginForm, SolicitacaoRedefinicaoSenhaForm, RedefinirSenhaForm
from .models import TokenRedefinicaoSenha
from utils.whatsapp import enviar_link_redefinicao_whatsapp

User = get_user_model()


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_empresa:
            return '/empresas/dashboard/'
        return '/concursos/'


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class SolicitarRedefinicaoSenhaView(View):
    template_name = 'accounts/solicitar_redefinicao.html'

    def get(self, request):
        return render(request, self.template_name, {'form': SolicitacaoRedefinicaoSenhaForm()})

    def post(self, request):
        form = SolicitacaoRedefinicaoSenhaForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        email = form.cleaned_data['email']
        canal = form.cleaned_data['canal']
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            messages.success(request, 'Se o e-mail estiver cadastrado, você receberá as instruções.')
            return redirect('solicitar_redefinicao_senha')

        token_obj = TokenRedefinicaoSenha.objects.create(usuario=user, canal=canal)
        link = f"{settings.BASE_URL}/accounts/redefinir-senha/{token_obj.token}/"

        if canal == TokenRedefinicaoSenha.CANAL_EMAIL:
            from django.core.mail import send_mail
            send_mail(
                subject='Redefinição de senha',
                message=f'Clique no link para redefinir sua senha:\n\n{link}\n\nO link expira em 2 horas.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
        else:
            try:
                candidato = user.candidato
                telefone_wpp = candidato.telefones.filter(tem_whatsapp=True).first()
                if telefone_wpp:
                    enviar_link_redefinicao_whatsapp(telefone_wpp.numero, link)
                else:
                    messages.error(request, 'Nenhum número com WhatsApp cadastrado.')
                    return render(request, self.template_name, {'form': form})
            except Exception:
                messages.error(request, 'Não foi possível enviar via WhatsApp.')
                return render(request, self.template_name, {'form': form})

        messages.success(request, 'Instruções enviadas com sucesso!')
        return redirect('solicitar_redefinicao_senha')


class RedefinirSenhaView(View):
    template_name = 'accounts/redefinir_senha.html'

    def _get_token(self, token_str):
        token_obj = get_object_or_404(TokenRedefinicaoSenha, token=token_str)
        if not token_obj.esta_valido():
            return None, token_obj
        return token_obj, None

    def get(self, request, token):
        token_obj, invalido = self._get_token(token)
        if invalido:
            messages.error(request, 'Link expirado ou já utilizado.')
            return redirect('solicitar_redefinicao_senha')
        return render(request, self.template_name, {
            'form': RedefinirSenhaForm(user=token_obj.usuario),
            'token': token,
        })

    def post(self, request, token):
        token_obj, invalido = self._get_token(token)
        if invalido:
            messages.error(request, 'Link expirado ou já utilizado.')
            return redirect('solicitar_redefinicao_senha')

        form = RedefinirSenhaForm(user=token_obj.usuario, data=request.POST)
        if form.is_valid():
            form.save()
            token_obj.usado = True
            token_obj.save()
            messages.success(request, 'Senha redefinida com sucesso! Faça login.')
            return redirect('login')
        return render(request, self.template_name, {'form': form, 'token': token})
