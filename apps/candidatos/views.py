from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

from .forms import CadastroUsuarioForm, CadastroCandidatoForm, TelefoneFormSet
from .models import Candidato

User = get_user_model()


def cadastro_candidato(request):
    if request.method == 'POST':
        user_form = CadastroUsuarioForm(request.POST)
        candidato_form = CadastroCandidatoForm(request.POST, request.FILES)
        # Instância temporária para o formset validar sem salvar ainda
        candidato_tmp = Candidato()
        telefone_formset = TelefoneFormSet(request.POST, instance=candidato_tmp)

        if user_form.is_valid() and candidato_form.is_valid() and telefone_formset.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password1'])
                user.tipo = User.CANDIDATO
                user.save()

                candidato = candidato_form.save(commit=False)
                candidato.usuario = user
                candidato.save()

                # Reatribui o formset com a instância salva
                telefone_formset = TelefoneFormSet(request.POST, instance=candidato)
                telefone_formset.is_valid()
                telefone_formset.save()

                login(request, user, backend='apps.accounts.backends.EmailBackend')
                messages.success(request, 'Cadastro realizado com sucesso! Bem-vindo(a).')
                return redirect('lista_concursos')
    else:
        user_form = CadastroUsuarioForm()
        candidato_form = CadastroCandidatoForm()
        telefone_formset = TelefoneFormSet()

    return render(request, 'candidatos/cadastro.html', {
        'user_form': user_form,
        'candidato_form': candidato_form,
        'telefone_formset': telefone_formset,
    })


@login_required
def perfil_candidato(request):
    if not hasattr(request.user, 'candidato'):
        messages.error(request, 'Perfil de candidato não encontrado.')
        return redirect('lista_concursos')

    candidato = request.user.candidato
    if request.method == 'POST':
        form = CadastroCandidatoForm(request.POST, request.FILES, instance=candidato)
        telefone_formset = TelefoneFormSet(request.POST, instance=candidato)
        if form.is_valid() and telefone_formset.is_valid():
            form.save()
            telefone_formset.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil_candidato')
    else:
        form = CadastroCandidatoForm(instance=candidato)
        telefone_formset = TelefoneFormSet(instance=candidato)

    return render(request, 'candidatos/perfil.html', {
        'form': form,
        'telefone_formset': telefone_formset,
        'candidato': candidato,
    })
