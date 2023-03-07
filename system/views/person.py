from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from system.models.company import Company
from system.models.person import Person
from system.models.event import Event
from system.models.register import Register
from system.forms import PersonForm


@login_required
def person_list(request):
    try:
        persons = Person.objects.all()
        data = {
            'persons': persons
        }
        return render(request, 'person/person_list.html', data)
    except:
        return('person_create')

@login_required
def person_create(request, id_company):
    company = Company.objects.get(id=id_company)
    form = PersonForm(request.POST or None)
    if form.is_valid():
        person = form.save(commit=False)
        person.company = company
        person.save()       
        return redirect('company_detail', company.id)
    data = {
        'form': form,
        'company': company
    }
    return render(request, 'person/person_create.html', data)


@login_required
def person_create_and_register(request, id_company, id_event):
    event = Event.objects.get(id=id_event)
    company = Company.objects.get(id=id_company)    
    form = PersonForm(request.POST or None)
    if form.is_valid():
        person = form.save(commit=False)
        person.company = company
        person.save()
        Register.objects.create(
            person=person,
            event=event,
            approved=True
        )
        messages.success(request, 'Participante incluído com sucesso')        
        return redirect('event_detail', id_event=id_event)
    data = {
        'form': form,
        'company': company,
        'event': event
    }
    return render(request, 'person/person_create_and_register.html', data)        

@login_required
def person_update(request, id):
    person = Person.objects.get(id=id)
    id_company = person.company.id
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('company_detail', id=id_company)
    data = {
        'form': form,
        'person': person
    }
    return render(request, 'person/person_update.html', data)

@login_required
def person_delete(request, id):
    company = Person.objects.get(id=id).company.id
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('company_detail', id=company)