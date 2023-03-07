from django.urls import path
from system.views.views import (
    home,
    # Credencial
    credential_maker,
    # Report
    report_generator,
)

from system.views.question import (
    question_list,
    question_by_event,
    question_approve,
    question_approved_by_event,
    question_delete,
    question_approved,
    question_clean,
)

from system.views.company import (
    company_create,
    company_list,
    company_update,
    company_detail,
    company_delete,
    company_approve,
    company_search,
)

from system.views.person import (
    person_list, person_create, person_create_and_register, person_update, person_delete,
)

from system.views.event import (
    event_list, event_create, event_update, event_delete, event_detail,
)

from system.views.register import (
    register, register_approve, register_delete,
)

from system.views.reffle import (
    raffle_prepare, raffle_event_list, raffle_maker, raffle_delete,
)

urlpatterns = [
    # Home
    path('', home, name="home"),

    # Question
    path("question/", question_list, name="question_list"),
    path("question/<int:id_event>", question_by_event, name="question_by_event"),
    path("question/<int:id_event>/<int:id_question>/approve/", question_approve, name="question_approve"),
    path("question/<int:id_event>/<int:id_question>/delete/",
         question_delete, name="question_delete"),
    path("question/approved/", question_approved, name="question_approved"),
    path("question/approved/<int:id_event>", question_approved_by_event, name="question_approved_by_event"),
    path("question/clean/<int:id_event>", question_clean, name="question_clean"),    

    # Company
    path("company/", company_list, name="company_list"),
    path("company/create/", company_create, name="company_create"),
    path("company/<int:id>/", company_detail, name="company_detail"),
    path("company/<int:id>/update/", company_update, name="company_update"),
    path("company/<int:id>/delete/", company_delete, name="company_delete"),
    path("company/<int:id>/approve/", company_approve, name="company_approve"),

    # Person
    path('person/', person_list, name='person_list'),
    path('company/<int:id_company>/person/create/',
         person_create, name='person_create'),
    path('company/<int:id_company>/person/create_and_register/<int:id_event>', person_create_and_register, name='person_create_and_register'),
    path("person/<int:id>/update/", person_update, name="person_update"),
    path('person/<int:id>/delete/', person_delete, name='person_delete'),

    # Event
    path('event/', event_list, name='event_list'),
    path('event/create/', event_create, name='event_create'),
    path('event/<int:id_event>/', event_detail, name='event_detail'),
    path("event/<int:id>/update/", event_update, name="event_update"),
    path("event/<int:id>/delete/", event_delete, name="event_delete"),

    #Raffle
    path('raffle/', raffle_event_list, name="raffle_event_list"),
    path('raffle/<int:id_event>', raffle_prepare, name="raffle_prepare"),
    path('raffle/<int:id_event>/maker', raffle_maker, name="raffle_maker"),
    path('raffle/<int:id_event>/delete/<int:id_winner>', raffle_delete, name='raffle_delete'),

    #Register
    path('register/<int:id_event>/person/', company_search, name="company_search"),
    path('register/<int:id_event>/person/<int:id_company>', register, name="register"),
    path('register/<int:id_register>/approve', register_approve, name="register_approve"),
    path('register/<int:id_register>/delete', register_delete, name="register_delete"),

    #Credential
    path('event/<int:id_event>/credential/<int:id_person>', credential_maker, name="credential_maker"),

    #Report
    path('event/<int:id_event>/report/', report_generator, name="report_generator"),
    
]
