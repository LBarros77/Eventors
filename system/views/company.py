from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from system.models.company import Company
from system.models.person import Person
from system.forms import CompanyForm
from system.filters import CompanyFilter


@login_required
def company_create(request):
    form = CompanyForm(request.POST or None)
    if str(request.method) == 'POST':
        try:
            if form.is_valid():
                company = form.save(commit=False)
                form.save()
                return redirect('company_detail', company.id)
        except:
            return('person_create')
    data = {
        'form': form
    }
    return render(request, 'company/company_create.html', data)

@login_required
def company_approve(request, id):
    company = Company.objects.get(id=id)
    company.approved = True
    company.save()
    return redirect('company_list')

@login_required
def company_list(request):
    try:
        cfilter = CompanyFilter(
            request.GET, queryset=Company.objects.all())
        data = {'cfilter': cfilter}
        return render(request, 'company/company_list.html', data)
    except:
        return redirect('company_create')

@login_required
def company_detail(request, id):
    company = Company.objects.get(id=id)
    persons = Person.objects.filter(company=company)
    data = {
        'company': company,
        'persons': persons
    }
    return render(request, 'company/company_detail.html', data)

@login_required
def company_update(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect('company_list')
    data = {
        'form': form,
        'company': company
    }
    return render(request, 'company/company_update.html', data)

@login_required
def company_delete(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect('company_list')

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
    return render(request, 'register/company_search.html', data)