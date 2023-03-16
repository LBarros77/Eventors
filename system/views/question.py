from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from system.models.question import Question
from system.models.event import Event


@login_required
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

@login_required
def question_list(request):
    try:
        events = Event.objects.all()
        return render(request, 'questions/questions.html', {'events': events})
    except:
        return render(request, 'base.html')

@login_required
def question_by_event(request, id_event):
    event = Event.objects.get(id=id_event)
    questions = Question.objects.filter(event=event)    
    return render(request, 'questions/question_list.html', {'questions': questions, 'event': event})  

@login_required
def question_approve(request, id_event, id_question):
    event = Event.objects.get(id=id_event)
    question = Question.objects.get(id=id_question)
    if question.approve == True:
        question.approve = False    
    else:
        question.approve = True        
    question.save()
    return redirect('question_by_event', id_event=id_event)

@login_required
def question_delete(request, id_event, id_question):
    event = Event.objects.get(id=id_event)
    question = Question.objects.get(id=id_question)
    question.delete()
    return redirect('question_by_event', id_event=id_event)


@login_required
def question_approved(request):
    try:
        events = Event.objects.all()
        return render(request, 'questions/question_approved.html', {'events': events})
    except:
        return render(request, 'base.html')

@login_required
def question_approved_by_event(request, id_event):
    events = Event.objects.get(id=id_event)
    question = Question.objects.filter(event=events, approve=True)
    return render(request, 'questions/question_approved_by_event.html', {'questions': question, 'events': events})

@login_required
def question_clean(request, id_event):
    event = Event.objects.get(id=id_event)
    question = Question.objects.filter(event=event)
    question.delete()
    return redirect('question_by_event', id_event=id_event)
