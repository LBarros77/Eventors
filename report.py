from system.models import *
import csv

event = Event.objects.get(id=2)
registers = Register.objects.filter(event=event)
with open('relatorio_noeli_linda.csv', mode='w') as report_umv:
    fieldnames = [
        'Nome',
        'E-mail',
        'Telefone',
        'Cargo',
        'Check-in',
        'Opt-in',
        'Empresa',
        'Razão Social',
        'Nome',
        'CNPJ',
        'Segmento',
        'Telefone',
        'CEP',
        'Logradouro',
        'Complemento'
        'Número',
        'Bairro',
        'Cidade',
        'Estado'
    ]
    writer = csv.DictWriter(report_umv, fieldnames=fieldnames)
    writer.writeheader()
    for register in registers:
        writer.writerow({
            'Nome': register.person.name,
            'E-mail': register.person.email,
            'Telefone': register.person.name,
            'Cargo': register.person.role,
            'Check-in': register.checkin,
            'Opt-in': register.person.opt_in,
            'Empresa': register.person.company.fantasy_name,
            'Razão Social':register.person.company.corporate_name,
            'CNPJ':register.person.company.cnpj,
            'Segmento':register.person.company.segmentation,
            'Telefone':register.person.company.phone,
            'CEP':register.person.company.cep,
            'Logradouro':register.person.company.public_place,
            'Complemento':register.person.company.complement,
            'Número':register.person.company.number,
            'Bairro':register.person.company.neighborhood,
            'Cidade':register.person.company.city,
            'Estado':register.person.company.state,
        })

