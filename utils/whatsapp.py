import re
from django.conf import settings


def enviar_link_redefinicao_whatsapp(numero: str, link: str) -> bool:
    try:
        from twilio.rest import Client
    except ImportError:
        raise ImportError("Instale o pacote 'twilio': pip install twilio")

    numero_formatado = _formatar_numero(numero)
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_=settings.TWILIO_WHATSAPP_FROM,
        to=f'whatsapp:{numero_formatado}',
        body=(
            f'*Redefinição de senha — ConcursosBR*\n\n'
            f'Clique no link abaixo para redefinir sua senha:\n{link}\n\n'
            f'O link expira em 2 horas. Se não foi você, ignore esta mensagem.'
        ),
    )
    return True


def _formatar_numero(numero: str) -> str:
    digitos = re.sub(r'\D', '', numero)
    if not digitos.startswith('55'):
        digitos = '55' + digitos
    return '+' + digitos
