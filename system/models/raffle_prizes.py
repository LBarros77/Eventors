from django.db import models
from .base import BaseModel


class RafflePrizes(BaseModel):
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE
    )