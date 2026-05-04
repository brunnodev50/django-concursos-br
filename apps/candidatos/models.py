from django.db import models
from django.conf import settings
from utils.validators import validar_cpf


def foto_upload_path(instance, filename):
    ext = filename.rsplit('.', 1)[-1]
    return f'fotos_candidatos/{instance.usuario.id}.{ext}'


class Candidato(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='candidato',
    )
    foto = models.ImageField(upload_to=foto_upload_path, verbose_name='Foto')
    nome_completo = models.CharField(max_length=200, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF', validators=[validar_cpf])
    rg = models.CharField(max_length=20, verbose_name='RG')
    orgao_emissor = models.CharField(max_length=20, verbose_name='Órgão Emissor')
    nome_mae = models.CharField(max_length=200, verbose_name='Nome da Mãe')
    nome_pai = models.CharField(max_length=200, verbose_name='Nome do Pai', blank=True)
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Renda Mensal (R$)')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def __str__(self):
        return self.nome_completo

    @property
    def email(self):
        return self.usuario.email


class Telefone(models.Model):
    CELULAR = 'celular'
    FIXO = 'fixo'
    TIPO_CHOICES = [
        (CELULAR, 'Celular'),
        (FIXO, 'Fixo'),
    ]

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField(max_length=20, verbose_name='Número')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=CELULAR)
    tem_whatsapp = models.BooleanField(default=False, verbose_name='Tem WhatsApp?')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        wpp = ' (WhatsApp)' if self.tem_whatsapp else ''
        return f'{self.numero} — {self.get_tipo_display()}{wpp}'
