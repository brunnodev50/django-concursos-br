from django.conf import settings


def _sdk():
    try:
        import mercadopago
    except ImportError:
        raise ImportError("Instale o pacote 'mercadopago': pip install mercadopago")
    return mercadopago.SDK(settings.MP_ACCESS_TOKEN)


def criar_pagamento_pix(valor: float, email: str, candidatura_id: int) -> dict:
    sdk = _sdk()
    payload = {
        'transaction_amount': valor,
        'payment_method_id': 'pix',
        'payer': {'email': email},
        'description': f'Taxa de inscrição — Candidatura #{candidatura_id}',
        'notification_url': f'{settings.BASE_URL}/pagamentos/webhook/mercadopago/',
    }
    resposta = sdk.payment().create(payload)
    if resposta['status'] not in (200, 201):
        raise Exception(f"Erro Mercado Pago: {resposta.get('response')}")
    return resposta['response']


def criar_pagamento_boleto(valor: float, email: str, cpf: str, nome: str, candidatura_id: int) -> dict:
    import re
    sdk = _sdk()
    cpf_limpo = re.sub(r'\D', '', cpf)
    payload = {
        'transaction_amount': valor,
        'payment_method_id': 'bolbradesco',
        'payer': {
            'email': email,
            'first_name': nome.split()[0],
            'last_name': ' '.join(nome.split()[1:]) or nome,
            'identification': {'type': 'CPF', 'number': cpf_limpo},
        },
        'description': f'Taxa de inscrição — Candidatura #{candidatura_id}',
        'notification_url': f'{settings.BASE_URL}/pagamentos/webhook/mercadopago/',
    }
    resposta = sdk.payment().create(payload)
    if resposta['status'] not in (200, 201):
        raise Exception(f"Erro Mercado Pago: {resposta.get('response')}")
    return resposta['response']
