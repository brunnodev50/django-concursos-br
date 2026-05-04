from django.db import models
from apps.candidaturas.models import Candidatura


class Pagamento(models.Model):
    BOLETO = 'boleto'
    PIX = 'pix'
    METODO_CHOICES = [
        (BOLETO, 'Boleto Bancário'),
        (PIX, 'PIX'),
    ]

    PENDENTE = 'pendente'
    PAGO = 'pago'
    CANCELADO = 'cancelado'
    EXPIRADO = 'expirado'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (PAGO, 'Pago'),
        (CANCELADO, 'Cancelado'),
        (EXPIRADO, 'Expirado'),
    ]

    candidatura = models.OneToOneField(Candidatura, on_delete=models.CASCADE, related_name='pagamento')
    metodo = models.CharField(max_length=10, choices=METODO_CHOICES)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=PENDENTE)

    # Dados Mercado Pago
    mp_payment_id = models.CharField(max_length=100, blank=True, verbose_name='ID Mercado Pago')
    mp_preference_id = models.CharField(max_length=100, blank=True)

    # PIX
    pix_qr_code = models.TextField(blank=True, verbose_name='QR Code PIX (base64)')
    pix_qr_code_texto = models.TextField(blank=True, verbose_name='Código PIX Copia e Cola')

    # Boleto
    boleto_url = models.URLField(blank=True, verbose_name='URL do Boleto')
    boleto_barcode = models.CharField(max_length=200, blank=True, verbose_name='Código de Barras')

    criado_em = models.DateTimeField(auto_now_add=True)
    pago_em = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-criado_em']

    def __str__(self):
        return f'Pagamento #{self.pk} — {self.candidatura}'
