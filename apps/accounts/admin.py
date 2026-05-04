from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, TokenRedefinicaoSenha


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'tipo', 'is_active', 'is_staff', 'criado_em')
    list_filter = ('tipo', 'is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('-criado_em',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Tipo', {'fields': ('tipo',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'tipo', 'password1', 'password2')}),
    )


@admin.register(TokenRedefinicaoSenha)
class TokenRedefinicaoSenhaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'canal', 'criado_em', 'usado')
    list_filter = ('canal', 'usado')
    readonly_fields = ('token', 'criado_em')
