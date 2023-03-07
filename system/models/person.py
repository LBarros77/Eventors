from django.db import models
from .base import BaseModel


OPT_IN_CHOICES = (
    ('0', 'Sim'),
    ('1', 'Não')
)

CATEGORY_CHOICES = (
    ('0', 'Visitente'),
    ('1', 'Expositor'),
    ('2', 'Apoio')
)

class Person(BaseModel):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    name_cracha = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False,
        default='0',
        max_length=3,
    )
    cell_phone = models.CharField(max_length=17)
    cpf = models.CharField(
        unique=True,
        max_length=14,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=254,
        blank=False,
        null=False
    )
    phone = models.CharField(
        max_length=17,
    )
    role = models.CharField(
        max_length=50,
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    opt_in = models.CharField(
        choices=OPT_IN_CHOICES,
        blank=False,
        null=False,
        max_length=3,
    )

    def __str__(self):
        return self.name
