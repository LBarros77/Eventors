from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from system.models.company import Company
from system.models.person import Person
from system.models.event import Event
from system.models.register import Register
from system.filters import CompanyFilter
from system.forms import CpfForm


@login_required
def register_approve(request, id_register):
    register = Register.objects.get(id=id_register)
    company = register.person.company
    event = register.event
    person = register.person
    if company.approved:
        if register.approved:
            register.approved = False
            register.save()
            messages.success(request, 'Status de aprovação alterado, o registro foi reprovado.')
            return redirect('event_detail', id_event=event.id)
        else:
            register.approved = True
            register.save()
            msg_html = render_to_string('mail/approved_person.html', {
                'person': person,
                'company': company,
                'event': event
            })
            send_mail(
                'Aprovação de registro',
                msg_html,
                'umv@appdoevento.com.br',
                [person.email],
                fail_silently=False,
                html_message=msg_html,
            )
            messages.success(request, 'Status de aprovação alterado, o registro foi aprovado.')        
            return redirect('event_detail', id_event=event.id)
    else:
        messages.success(request, 'Empresa do participante ainda não foi aprovada. Aprove a empresa para continuar com o processo.')              
        return redirect('event_detail', id_event=event.id)

@login_required
def register_delete(request, id_register):
    register = Register.objects.get(id=id_register)
    event = register.event
    register.delete()
    messages.success(request, 'Registro excluído com sucesso!')
    return redirect(event_detail, id_event=event.id)

@login_required
def register(request, id_event, id_company):  
    company = Company.objects.get(id=id_company)
    event = Event.objects.get(id=id_event)
    form = CpfForm(request.POST or None)
    if form.is_valid():
        try:
            person = Person.objects.get(cpf=form.cleaned_data['cpf'])
        except:
            person = None
        if person:
            registered = Register.objects.filter(
                person=person, event=event).count()
            current_stocking = Register.objects.filter(event=event).count()
            if  current_stocking < event.qtd_registration:
                if registered == 0:
                    Register.objects.create(
                        person=person,
                        event=event
                    )
                    messages.success(request, 'Registro efetuado com sucesso!')
                    return redirect('event_detail', id_event=event.id)
                else:
                    messages.success(request, 'Usuário já resgistrado neste evento!')
                    return redirect('event_detail', id_event=event.id)
            else:
                messages.success(request, 'Evento atingiu a lotação máxima, remova participantes ou aumente a capadidade do evento')
                return redirect('event_detail', id_event=event.id)
        else:
            return redirect('person_create_and_register', id_company=company.id, id_event=event.id)
    return render(request, 'register/register.html', {'form': form, 'event': event, 'company': company})
