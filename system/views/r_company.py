from django.shortcuts import render, redirect
from system.models.event import Event
from system.models.person import Person
from system.models.register import Register
from system.models.company import Company
from system.models.check_in import CheckIn
from system.forms import CompanyForm, PersonForm, QuestionForm, CnpjForm, CpfForm
from system.filters import CompanyFilter
from datetime import date
from django.contrib import messages


def r_company_create(request, id_event):
    event = Event.objects.get(id=id_event)
    form = CompanyForm(request.POST or None)
    person = Person.objects.get(id=1)
    if form.is_valid():
        company = form.save(commit=False)
        person.company = company
        company.save()
        current_stocking = Register.objects.filter(event=event).count()
        if  current_stocking < event.qtd_registration:
            Register.objects.create(
                person=person,
                event=event
            )
            return render(request, 'register/register_success.html')
        else:
            return render(request, 'register/max_stocking.html', {'event': event})
    data = {
        'form': form,
        'event': event
    }
    return render(request, 'register/r_company_create.html', data)

def r_company_detail(request, id):
    company = Company.objects.get(id=id)
    data = {
        'company': company,
    }
    return render(request, 'register/r_company_detail.html', data)

def r_company_search(request, id_event):
    event = Event.objects.get(id=id_event)
    form = CompanyForm(request.POST or None)
    form1 = CnpjForm(request.POST or None)
    cfilter = CompanyFilter(
        request.GET, queryset=Company.objects.filter(approved=True))
    num_results = Company.objects.filter(approved=True).count()
    data = {
        'cfilter': cfilter,
        'num_results': num_results,
        'event': event,
        'option': False
    }
    if str(request.method) == 'POST':
        if form1.is_valid():
            cnpj = form1.cleaned_data['cnpj']
            # check = form1.cleaned_data['term_check']
            if Company.objects.filter(cnpj=cnpj):
                data['option'] = True
                return render(request, 'register/register_lb.html', data)
            return render(request, 'register/r_company_create.html', {'form': form, 'event': event})
        # messages.error(request, 'Formulário invalido') 
    return render(request, 'register/register_lb.html', data)