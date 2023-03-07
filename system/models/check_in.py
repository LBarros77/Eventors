from django.db import models
from .base import BaseModel


class CheckIn(BaseModel):
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
    register = models.ForeignKey(
        'Register',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.person.name + ' - ' + self.event.title
        