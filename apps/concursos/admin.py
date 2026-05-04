from django.contrib import admin
from .models import Concurso, Cargo, Edital


class CargoInline(admin.TabularInline):
    model = Cargo
    extra = 0


class EditalInline(admin.TabularInline):
    model = Edital
    extra = 0
    readonly_fields = ('data_publicacao',)


@admin.register(Concurso)
class ConcursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'estado', 'cidade', 'status', 'data_fechamento')
    list_filter = ('status', 'estado')
    search_fields = ('titulo', 'orgao', 'cidade')
    inlines = [CargoInline, EditalInline]
    readonly_fields = ('criado_em', 'atualizado_em')
    actions = ['publicar_concursos', 'encerrar_concursos']

    @admin.action(description='Publicar concursos selecionados')
    def publicar_concursos(self, request, queryset):
        queryset.update(status=Concurso.ABERTO)

    @admin.action(description='Encerrar concursos selecionados')
    def encerrar_concursos(self, request, queryset):
        queryset.update(status=Concurso.ENCERRADO)
