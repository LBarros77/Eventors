from django.db import models
from .base import BaseModel


class Register(BaseModel):
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    approved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.person.name + ' - ' + self.event.title    
    
    @property
    def checked_in(self):              
        checked_in = CheckIn.objects.filter(person=self.person).count()
        if checked_in > 0:
            return True
        else:
            return False
    @property
    def checkin(self):
        if self.checked_in:
            return "Sim"
        else:
            return "Não"    
    @property
    def status(self):
        if self.approved == True:
            return "Aprovado"
        else:
            return "Reprovado"    
