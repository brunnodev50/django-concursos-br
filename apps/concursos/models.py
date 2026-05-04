from django.db import models
from apps.empresas.models import Empresa

ESTADOS_BR = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
]


def edital_upload_path(instance, filename):
    return f'editais/concurso_{instance.concurso.id}/{filename}'


class Concurso(models.Model):
    RASCUNHO = 'rascunho'
    ABERTO = 'aberto'
    ENCERRADO = 'encerrado'
    SUSPENSO = 'suspenso'
    STATUS_CHOICES = [
        (RASCUNHO, 'Rascunho'),
        (ABERTO, 'Aberto'),
        (ENCERRADO, 'Encerrado'),
        (SUSPENSO, 'Suspenso'),
    ]

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='concursos')
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    orgao = models.CharField(max_length=200, verbose_name='Órgão/Instituição')
    estado = models.CharField(max_length=2, choices=ESTADOS_BR, verbose_name='Estado')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    vagas_total = models.PositiveIntegerField(verbose_name='Total de Vagas')
    taxa_inscricao = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Taxa de Inscrição (R$)')
    data_abertura = models.DateField(verbose_name='Data de Abertura')
    data_fechamento = models.DateField(verbose_name='Data de Fechamento')
    data_prova = models.DateField(verbose_name='Data da Prova', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=RASCUNHO)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Concurso'
        verbose_name_plural = 'Concursos'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

    @property
    def esta_aberto(self):
        return self.status == self.ABERTO


class Cargo(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE, related_name='cargos')
    nome = models.CharField(max_length=200, verbose_name='Nome do Cargo')
    nivel_escolaridade = models.CharField(max_length=100, verbose_name='Nível de Escolaridade')
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário (R$)')
    vagas = models.PositiveIntegerField(verbose_name='Vagas')
    vagas_pcd = models.PositiveIntegerField(default=0, verbose_name='Vagas PCD')

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return f'{self.nome} — {self.concurso.titulo}'


class Edital(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE, related_name='editais')
    titulo = models.CharField(max_length=200, verbose_name='Título do Edital')
    arquivo = models.FileField(upload_to=edital_upload_path, verbose_name='Arquivo (PDF)')
    data_publicacao = models.DateField(verbose_name='Data de Publicação', auto_now_add=True)
    retificacao = models.BooleanField(default=False, verbose_name='É Retificação?')

    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'
        ordering = ['-data_publicacao']

    def __str__(self):
        return f'{self.titulo} — {self.concurso.titulo}'
