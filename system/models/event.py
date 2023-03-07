from django.db import models
from .base import BaseModel


class Event(BaseModel):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    description = models.TextField()
    cep = models.CharField(
        max_length=17,
        null=False,
        blank=False,
    )
    public_place = models.CharField(
        max_length=249,
        blank=False,
        null=False,
    )
    complement = models.CharField(
        max_length=249,
        blank=True,
        null=True,
    )
    neighborhood = models.CharField(
        max_length=80,
        blank=False,
        null=False,
    )
    city = models.CharField(
        max_length=80,
        blank=False,
        null=False,
    )
    state = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )
    number = models.IntegerField(
        null=False,
        blank=False,
    )
    first_date = models.DateField(
        auto_now=False,
    )
    first_hour = models.TimeField(
        auto_now=False,
    )
    last_date = models.DateField(
        auto_now=False,
    )
    last_hour = models.TimeField(
        auto_now=False,
    )
    qtd_registration = models.IntegerField(
        null=False,
        blank=False,
        default=10
    )

    def __str__(self):
        return self.title
