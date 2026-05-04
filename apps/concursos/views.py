from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q

from .models import Concurso, Edital
from .forms import ConcursoForm, CargoFormSet, EditalForm, FiltroConcursoForm


def lista_concursos(request):
    concursos = Concurso.objects.filter(status=Concurso.ABERTO).select_related('empresa')
    form = FiltroConcursoForm(request.GET)

    if form.is_valid():
        q = form.cleaned_data.get('q')
        estado = form.cleaned_data.get('estado')
        cidade = form.cleaned_data.get('cidade')
        if q:
            concursos = concursos.filter(
                Q(titulo__icontains=q) | Q(orgao__icontains=q) | Q(descricao__icontains=q)
            )
        if estado:
            concursos = concursos.filter(estado=estado)
        if cidade:
            concursos = concursos.filter(cidade__icontains=cidade)

    paginator = Paginator(concursos, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'concursos/lista.html', {
        'page_obj': page_obj,
        'concursos': page_obj,
        'form': form,
        'total': paginator.count,
    })


def detalhe_concurso(request, pk):
    concurso = get_object_or_404(Concurso, pk=pk)
    ja_candidatou = False
    if request.user.is_authenticated and hasattr(request.user, 'candidato'):
        ja_candidatou = concurso.candidaturas.filter(candidato=request.user.candidato).exists()
    return render(request, 'concursos/detalhe.html', {
        'concurso': concurso,
        'ja_candidatou': ja_candidatou,
    })


@login_required
def criar_concurso(request):
    if not request.user.is_empresa:
        messages.error(request, 'Acesso restrito a empresas.')
        return redirect('lista_concursos')
    empresa = request.user.empresa

    if request.method == 'POST':
        form = ConcursoForm(request.POST)
        if form.is_valid():
            concurso = form.save(commit=False)
            concurso.empresa = empresa
            cargo_formset = CargoFormSet(request.POST, instance=concurso)
            if cargo_formset.is_valid():
                with transaction.atomic():
                    concurso.save()
                    cargo_formset.instance = concurso
                    cargo_formset.save()
                messages.success(request, 'Concurso criado com sucesso!')
                return redirect('detalhe_concurso', pk=concurso.pk)
        else:
            cargo_formset = CargoFormSet(request.POST)
    else:
        form = ConcursoForm()
        cargo_formset = CargoFormSet()

    return render(request, 'empresas/concurso_form.html', {
        'form': form,
        'cargo_formset': cargo_formset,
    })


@login_required
def editar_concurso(request, pk):
    if not request.user.is_empresa:
        return redirect('lista_concursos')
    concurso = get_object_or_404(Concurso, pk=pk, empresa=request.user.empresa)

    if request.method == 'POST':
        form = ConcursoForm(request.POST, instance=concurso)
        cargo_formset = CargoFormSet(request.POST, instance=concurso)
        if form.is_valid() and cargo_formset.is_valid():
            with transaction.atomic():
                form.save()
                cargo_formset.save()
            messages.success(request, 'Concurso atualizado com sucesso!')
            return redirect('detalhe_concurso', pk=concurso.pk)
    else:
        form = ConcursoForm(instance=concurso)
        cargo_formset = CargoFormSet(instance=concurso)

    return render(request, 'empresas/concurso_form.html', {
        'form': form,
        'cargo_formset': cargo_formset,
        'concurso': concurso,
    })


@login_required
def upload_edital(request, pk):
    if not request.user.is_empresa:
        return redirect('lista_concursos')
    concurso = get_object_or_404(Concurso, pk=pk, empresa=request.user.empresa)

    if request.method == 'POST':
        form = EditalForm(request.POST, request.FILES)
        if form.is_valid():
            edital = form.save(commit=False)
            edital.concurso = concurso
            edital.save()
            messages.success(request, 'Edital publicado com sucesso!')
            return redirect('detalhe_concurso', pk=concurso.pk)
    else:
        form = EditalForm()

    return render(request, 'concursos/edital_form.html', {'form': form, 'concurso': concurso})
