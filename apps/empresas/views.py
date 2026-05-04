from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

from .forms import CadastroEmpresaUsuarioForm, CadastroEmpresaForm
from apps.concursos.models import Concurso

User = get_user_model()


def cadastro_empresa(request):
    if request.method == 'POST':
        user_form = CadastroEmpresaUsuarioForm(request.POST)
        empresa_form = CadastroEmpresaForm(request.POST)
        if user_form.is_valid() and empresa_form.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password1'])
                user.tipo = User.EMPRESA
                user.save()
                empresa = empresa_form.save(commit=False)
                empresa.usuario = user
                empresa.save()
                login(request, user, backend='apps.accounts.backends.EmailBackend')
                messages.success(request, 'Empresa cadastrada com sucesso!')
                return redirect('dashboard_empresa')
    else:
        user_form = CadastroEmpresaUsuarioForm()
        empresa_form = CadastroEmpresaForm()

    return render(request, 'empresas/cadastro.html', {
        'user_form': user_form,
        'empresa_form': empresa_form,
    })


@login_required
def dashboard_empresa(request):
    if not request.user.is_empresa:
        return redirect('lista_concursos')
    empresa = request.user.empresa
    concursos = Concurso.objects.filter(empresa=empresa).order_by('-criado_em')
    return render(request, 'empresas/dashboard.html', {'empresa': empresa, 'concursos': concursos})
