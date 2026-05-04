from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.concursos.models import Concurso
from .models import Candidatura
from .forms import CandidaturaForm


@login_required
def candidatar(request, concurso_pk):
    if not hasattr(request.user, 'candidato'):
        messages.error(request, 'Apenas candidatos podem se inscrever.')
        return redirect('detalhe_concurso', pk=concurso_pk)

    concurso = get_object_or_404(Concurso, pk=concurso_pk, status=Concurso.ABERTO)
    candidato = request.user.candidato

    if Candidatura.objects.filter(candidato=candidato, concurso=concurso).exists():
        messages.warning(request, 'Você já se candidatou a este concurso.')
        return redirect('detalhe_concurso', pk=concurso_pk)

    if request.method == 'POST':
        form = CandidaturaForm(concurso, request.POST)
        if form.is_valid():
            candidatura = form.save(commit=False)
            candidatura.candidato = candidato
            candidatura.concurso = concurso
            candidatura.status = Candidatura.AGUARDANDO_PAGAMENTO
            candidatura.save()
            return redirect('checkout_pagamento', candidatura_pk=candidatura.pk)
    else:
        form = CandidaturaForm(concurso)

    return render(request, 'candidaturas/confirmar.html', {
        'concurso': concurso,
        'form': form,
    })


@login_required
def minhas_candidaturas(request):
    candidato = request.user.candidato
    candidaturas = candidato.candidaturas.select_related('concurso', 'cargo').all()
    return render(request, 'candidaturas/minhas.html', {'candidaturas': candidaturas})
