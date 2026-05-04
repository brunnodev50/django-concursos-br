from django.db import models
from django.conf import settings
from utils.validators import validar_cnpj


class Empresa(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='empresa',
    )
    razao_social = models.CharField(max_length=200, verbose_name='Razão Social')
    nome_fantasia = models.CharField(max_length=200, verbose_name='Nome Fantasia', blank=True)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ', validators=[validar_cnpj])
    responsavel = models.CharField(max_length=200, verbose_name='Nome do Responsável')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razao_social
