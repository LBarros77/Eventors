from django.contrib import admin
from .models.check_in import CheckIn
from .models.company import Company
from .models.event import Event
from .models.person import Person
from .models.question import Question
from .models.raffle_prizes import RafflePrizes
from .models.register import Register

admin.site.register(CheckIn)
admin.site.register(Company)
admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Question)
admin.site.register(RafflePrizes)
admin.site.register(Register)
