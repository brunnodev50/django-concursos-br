from django.contrib import admin
from .models import Candidato, Telefone


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 0


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'email', 'criado_em')
    search_fields = ('nome_completo', 'cpf', 'usuario__email')
    inlines = [TelefoneInline]
    readonly_fields = ('criado_em', 'atualizado_em')
