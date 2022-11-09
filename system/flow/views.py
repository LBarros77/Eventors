from django.shortcuts import render, redirect
from system.models import Event, Person, Register, Company, CheckIn
from system.forms import CompanyForm, PersonForm, QuestionForm, CnpjForm, CpfForm
from system.filters import CompanyFilter
from datetime import date
from django.contrib import messages


def r_register(request, id_event, id_company):
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
                    return render(request, 'register/register_success.html')
                else:
                    return render(request, 'register/register_waiting_approval.html', {'event': event})
            else:
                return render(request, 'register/max_stocking.html', {'event': event})
        else:
            return redirect('r_person_create', id_event=event.id)
    return render(request, 'register/r_register.html', {'form': form, 'event': event, 'company': company})


def r_company_detail(request, id):
    company = Company.objects.get(id=id)
    data = {
        'company': company,
    }
    return render(request, 'register/r_company_detail.html', data)


def r_company_create(request, id_event):
    event = Event.objects.get(id=id_event)
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        company = form.save(commit=False)
        form.save()
        return redirect('r_register', id_event=event.id, id_company=company.id)
    data = {
        'form': form,
        'event': event
    }
    return render(request, 'register/r_company_create.html', data)


def r_person_create(request, id_company, id_event):
    event = Event.objects.get(id=id_event)
    form = PersonForm(request.POST or None)
    company = Company.objects.get(id=id_company)
    if form.is_valid():
        person = form.save(commit=False)
        person.company = company
        person.save()
        Register.objects.create(
            person=person,
            event=event
        )
        return render(request, 'register/r_person_create_success.html',{'event':event})
    data = {
        'form': form,
        'company': company,
        'event': event
    }
    return render(request, 'register/r_person_create.html', data)


def checkin(request, id):
    event = Event.objects.get(id=id)
    form = CpfForm(request.POST or None)

    if form.is_valid():
        try:
            person = Person.objects.get(cpf=form.cleaned_data['cpf'])
        except:
            person = None
        if person:
            try:
                registered = Register.objects.get(
                    event=event, person=person)
            except:
                registered = None
            if registered:
                if not registered.approved:
                    return render(request, 'register/register_waiting_approval.html', {'event': event})
                else:    
                    if registered.checked_in:
                        return render(request, 'checkin/already_checkin.html', {'event': event})                                            
                CheckIn.objects.create(
                    person=person,
                    event=event,
                    register=registered
                )
                return render(request, 'checkin/checkin_success.html', {'event': event})                  
            else:
                return render(request, 'checkin/checkin_fail.html', {'event': event})
        else:
            return redirect('r_company_search', event.id)
    return render(request, 'checkin/checkin.html', {'form': form, 'event': event})


def question_create(request, id):
    event = Event.objects.get(id=id)
    current_day = date.today()
    form = QuestionForm(request.POST or None)
    if current_day > event.last_date:
        return render(request, 'register/r_event_expired.html', {'event': event }) 
    if form.is_valid():    
        instance = form.save(commit=False)
        instance.event = event
        instance.save()
        return render(request, 'questions/question_success.html', {'event': event})
    return render(request, 'questions/question_create.html', {'form': form, 'event': event })


def company_search(request, id_event):
    event = Event.objects.get(id=id_event)
    cfilter = CompanyFilter(
        request.GET, queryset=Company.objects.filter(approved=True))
    num_results = Company.objects.filter(approved=True).count()
    data = {
        'cfilter': cfilter,
        'num_results': num_results,
        'event': event
    }
    return render(request, 'register/register_lb.html', data)


def company_create(request, id_event):
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


def person_create(request, id_event):
    event = Event.objects.get(id=id_event)
    form = PersonForm(request.POST or None)
    company = Company.objects.get(id=1)
    if form.is_valid():
        person = form.save(commit=False)
        person.company = company
        person.save()
        current_stocking = Register.objects.filter(event=event).count()
        if  current_stocking < event.qtd_registration:
            Register.objects.create(
                person=person,
                event=event
            )
            # return render(request, 'register/r_person_create_success.html',{'event':event})
            return render(request, 'register/register_success.html')
        else:
            return render(request, 'register/max_stocking.html', {'event': event})
    data = {
        'form': form,
        'company': company,
        'event': event
    }
    return render(request, 'register/r_person_create.html', data)


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