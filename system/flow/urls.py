from django.urls import path
from system.flow.views import (
    r_register, r_company_detail,
    r_company_create, checkin, r_person_create,
    question_create, r_company_search
)


urlpatterns = [
    path('register/<int:id_event>/', r_company_search, name='r_company_search'),
    path('register/<int:id_event>/person/<int:id_company>', r_register, name='r_register'),
#    path('companies/search/', r_company_search, name='r_company_search'),
    path("question/create/<int:id>", question_create, name="question_create"),
    path('companies/<int:id>/', r_company_detail, name='r_company_detail'),
    path('company/create/<int:id_event>/', r_company_create, name='r_company_create'),
    path('company/person/create/<int:id_event>', r_person_create, name='r_person_create'),
    path('checkin/<int:id>/', checkin, name='checkin')
]
