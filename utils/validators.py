import re
from django.core.exceptions import ValidationError


def _apenas_digitos(valor):
    return re.sub(r'\D', '', valor)


def validar_cpf(valor):
    cpf = _apenas_digitos(valor)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido.')

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            raise ValidationError('CPF inválido.')


def validar_cnpj(valor):
    cnpj = _apenas_digitos(valor)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        raise ValidationError('CNPJ inválido.')

    def calcular_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    if calcular_digito(cnpj, pesos1) != int(cnpj[12]):
        raise ValidationError('CNPJ inválido.')
    if calcular_digito(cnpj, pesos2) != int(cnpj[13]):
        raise ValidationError('CNPJ inválido.')
