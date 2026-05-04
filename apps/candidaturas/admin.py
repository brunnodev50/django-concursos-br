from django.contrib import admin
from .models import Candidatura


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'concurso', 'cargo', 'status', 'numero_inscricao', 'criado_em')
    list_filter = ('status', 'concurso__estado')
    search_fields = ('candidato__nome_completo', 'concurso__titulo', 'numero_inscricao')
    readonly_fields = ('numero_inscricao', 'criado_em', 'atualizado_em')
