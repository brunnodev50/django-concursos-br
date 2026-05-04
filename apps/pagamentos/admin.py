from django.contrib import admin
from .models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('candidatura', 'metodo', 'valor', 'status', 'criado_em', 'pago_em')
    list_filter = ('metodo', 'status')
    search_fields = ('candidatura__candidato__nome_completo', 'mp_payment_id')
    readonly_fields = ('criado_em', 'pago_em', 'mp_payment_id', 'pix_qr_code', 'pix_qr_code_texto', 'boleto_url', 'boleto_barcode')
