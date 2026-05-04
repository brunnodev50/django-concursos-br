from django.db import models
from apps.candidatos.models import Candidato
from apps.concursos.models import Concurso, Cargo


class Candidatura(models.Model):
    PENDENTE = 'pendente'
    AGUARDANDO_PAGAMENTO = 'aguardando_pagamento'
    PAGA = 'paga'
    CANCELADA = 'cancelada'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (AGUARDANDO_PAGAMENTO, 'Aguardando Pagamento'),
        (PAGA, 'Paga / Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='candidaturas')
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE, related_name='candidaturas')
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, related_name='candidaturas')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=PENDENTE)
    numero_inscricao = models.CharField(max_length=20, unique=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Candidatura'
        verbose_name_plural = 'Candidaturas'
        unique_together = ('candidato', 'concurso')
        ordering = ['-criado_em']

    def save(self, *args, **kwargs):
        if not self.numero_inscricao:
            import uuid
            self.numero_inscricao = str(uuid.uuid4()).replace('-', '')[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.candidato.nome_completo} → {self.concurso.titulo}'
