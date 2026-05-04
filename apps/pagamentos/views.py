import json
import hmac
import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.conf import settings

from apps.candidaturas.models import Candidatura
from .models import Pagamento
from utils.mercadopago_client import criar_pagamento_pix, criar_pagamento_boleto


@login_required
def checkout(request, candidatura_pk):
    candidatura = get_object_or_404(
        Candidatura,
        pk=candidatura_pk,
        candidato=request.user.candidato,
        status=Candidatura.AGUARDANDO_PAGAMENTO,
    )

    if hasattr(candidatura, 'pagamento') and candidatura.pagamento.status == Pagamento.PAGO:
        return redirect('minhas_candidaturas')

    if request.method == 'POST':
        metodo = request.POST.get('metodo')
        candidato = candidatura.candidato
        valor = float(candidatura.concurso.taxa_inscricao)
        email = candidato.email

        try:
            if metodo == Pagamento.PIX:
                dados = criar_pagamento_pix(valor, email, candidatura.pk)
                pagamento = Pagamento.objects.update_or_create(
                    candidatura=candidatura,
                    defaults={
                        'metodo': Pagamento.PIX,
                        'valor': valor,
                        'status': Pagamento.PENDENTE,
                        'mp_payment_id': str(dados.get('id', '')),
                        'pix_qr_code': dados.get('point_of_interaction', {}).get('transaction_data', {}).get('qr_code_base64', ''),
                        'pix_qr_code_texto': dados.get('point_of_interaction', {}).get('transaction_data', {}).get('qr_code', ''),
                    },
                )[0]
            elif metodo == Pagamento.BOLETO:
                dados = criar_pagamento_boleto(valor, email, candidato.cpf, candidato.nome_completo, candidatura.pk)
                pagamento = Pagamento.objects.update_or_create(
                    candidatura=candidatura,
                    defaults={
                        'metodo': Pagamento.BOLETO,
                        'valor': valor,
                        'status': Pagamento.PENDENTE,
                        'mp_payment_id': str(dados.get('id', '')),
                        'boleto_url': dados.get('transaction_details', {}).get('external_resource_url', ''),
                        'boleto_barcode': dados.get('barcode', {}).get('content', ''),
                    },
                )[0]
            else:
                messages.error(request, 'Método de pagamento inválido.')
                return redirect('checkout_pagamento', candidatura_pk=candidatura_pk)

            return redirect('confirmacao_pagamento', pagamento_pk=pagamento.pk)

        except Exception as e:
            messages.error(request, f'Erro ao processar pagamento: {e}')

    return render(request, 'pagamentos/checkout.html', {'candidatura': candidatura})


@login_required
def confirmacao(request, pagamento_pk):
    pagamento = get_object_or_404(
        Pagamento,
        pk=pagamento_pk,
        candidatura__candidato=request.user.candidato,
    )
    return render(request, 'pagamentos/confirmacao.html', {'pagamento': pagamento})


@csrf_exempt
def webhook_mercadopago(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    payload = request.body
    sig_header = request.headers.get('x-signature', '')
    secret = settings.MP_WEBHOOK_SECRET.encode()

    try:
        expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, sig_header):
            return HttpResponse(status=400)
    except Exception:
        return HttpResponse(status=400)

    data = json.loads(payload)
    if data.get('type') == 'payment':
        payment_id = str(data.get('data', {}).get('id', ''))
        try:
            pagamento = Pagamento.objects.get(mp_payment_id=payment_id)
            from utils.mercadopago_client import _sdk
            sdk = _sdk()
            resultado = sdk.payment().get(int(payment_id))
            status_mp = resultado.get('response', {}).get('status')
            if status_mp == 'approved':
                pagamento.status = Pagamento.PAGO
                pagamento.pago_em = timezone.now()
                pagamento.save()
                pagamento.candidatura.status = Candidatura.PAGA
                pagamento.candidatura.save()
        except Pagamento.DoesNotExist:
            pass

    return HttpResponse(status=200)
