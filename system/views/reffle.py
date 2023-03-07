from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import random
from system.models.person import Person
from system.models.event import Event
from system.models.raffle_prizes import RafflePrizes
from system.models.check_in import CheckIn


@login_required
def raffle_event_list(request):
    try:
        events = Event.objects.all()
        return render(request, 'raffle/raffle.html', {'events': events})
    except:
        return render(request, 'base.html')

@login_required
def raffle_prepare(request, id_event):
    event = Event.objects.get(id=id_event)
    checkeds_in = CheckIn.objects.filter(event=event)
    winners = RafflePrizes.objects.filter(event=event)
    return render(request, 'raffle/make_raffle.html', {'event': event, 'checkeds_in':checkeds_in, 'winners':winners })

@login_required
def raffle_maker(request, id_event):
    event = Event.objects.get(id=id_event)
    checkeds_in = CheckIn.objects.filter(event=event)
    participants = []

    for people in checkeds_in:
        participants.append(people.person.id)
    id_winner = random.choice(participants)
    winner = Person.objects.get(id=id_winner)

    already_won = RafflePrizes.objects.filter(person=winner).count()
    qtd_winners = RafflePrizes.objects.filter(event=event).count()
    qtd_participants = CheckIn.objects.filter(event=event).count()
    if qtd_participants > qtd_winners:
        if already_won == 0:
            RafflePrizes.objects.create(
                event=event,
                person=winner
            )
        else:
            raffle_maker(request, event.id)        
    return redirect('raffle_prepare', id_event=id_event)


@login_required
def raffle_delete(request, id_event, id_winner):
    event = Event.objects.get(id=id_event)
    person = Person.objects.get(id=id_winner)
    delete = RafflePrizes.objects.filter(event=event, person=person)
    delete.delete()
    return redirect('raffle_prepare', id_event=id_event)
