from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from system.models.person import Person
from system.models.event import Event
from system.models.register import Register
from openpyxl import Workbook


@login_required
def home(request):
    return render(request, 'home/welcome.html')


def credential_maker(request, id_event, id_person):
    person = get_object_or_404(Person, id=id_person)
    event = Event.objects.get(id=id_event)
    return render(request, 'credential/credential.html', {'person': person, 'event':event })


@login_required
def report_generator(request, id_event):
    event = Event.objects.get(id=id_event)
    registers = Register.objects.filter(event=event)
    
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename=Report_UMV.xlsx'

    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = "Relatório do evento " + event.title

    columns = [
        'Nome',
        'E-mail',
        'Telefone',
        'Cargo',
        'Empresa',
        'CNPJ',
        'Check-in',
        'Inscrição'
    ]

    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for register in registers:
        row_num += 1
        row = [
            register.person.name,
            register.person.email,
            register.person.phone,
            register.person.role,
            register.person.company.fantasy_name,
            register.person.company.cnpj,
            register.checkin,
            register.status
        ]
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response            

