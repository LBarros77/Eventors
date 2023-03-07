from django.db import models
from .base import BaseModel


class Question(BaseModel):
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    question = models.TextField(
        max_length=100,
        blank=False,
        null=False
    )
    approve = models.BooleanField(
        default=False
    )
    
    def __str__(self):
        return self.name