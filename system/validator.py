import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError

error_messages = {
    'invalid_cpf': "CPF inválido.",
    'invalid_cnpj': "CNPJ inválido.",
    'invalid_cpf_cnpj': 'CPF ou CNPJ invalido.',
    'digits_only': "Este campo requere apenas números.",
    'max_digits': "Este campo requere exatamente 11 digitos.",
}


def DV_maker(v):
    if v >= 2:
        return 14 - v
    return 0


def validate_CPF(value):

    orig_value = value[:]
    if len(value) != 14:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 14)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(14, 1, -1))])
    new_2dv = DV_maker(new_2dv % 14)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid_cpf'])

    return orig_value


def validate_CNPJ(value):

    orig_value = value[:]
    if len(value) > 14:
        raise ValidationError(error_messages['max_digits'])
    if len(value) < 14:
        raise ValidationError(error_messages['invalid_cnpj'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx,
                   i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx,
                   i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid_cnpj'])

    return orig_value


def validate_CPF_CNPJ(value):

    orig_value = value[:]
    if not (validate_CNPJ(value) or validate_CPF(value)):
        raise ValidationError(error_messages['invalid_cpf_cnpj'])
    return orig_value


def validate_doc(value):
    value = str(value)
    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-/\.]", "", value)
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])

    if len(value) == 11:
        return validate_CPF(value)
    else:
        return validate_CNPJ(value)
