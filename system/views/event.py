from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from system.models.event import Event
from system.models.register import Register
from system.forms import EventForm


@login_required
def event_list(request):
    try:
        events = Event.objects.all()
        data = {'events': events}
        return render(request, 'event/event_list.html', data)
    except:
        return redirect('event_create')

@login_required
def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    data = {
        'form': form
    }
    return render(request, 'event/event_create.html', data)

@login_required
def event_update(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    data = {
        'form': form,
        'event': event
    }
    return render(request, 'event/event_update.html', data)

@login_required
def event_detail(request, id_event):
    event = Event.objects.get(id=id_event)
    registers = Register.objects.filter(event=event)
    data = {
        'event': event,
        'registers': registers
    }
    return render(request, 'event/event_detail.html', data)

@login_required
def event_delete(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('event_list')
