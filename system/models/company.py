from django.db import models
from .base import BaseModel


SEGMENTATION_CHOICES = (
    ('0', 'Sem Segmento'),
    ('1', 'Informática'),
    ('2', 'Eletro'),
    ('3', 'Materiais de Construção'),
    ('4', 'Veterinário'),
    ('5', 'Varejo Alimentar'),
    ('6', 'Farma')
)

class Company(BaseModel):
    company_name = models.CharField(max_length=140)
    corporate_name = models.CharField(
        max_length=140,
        blank=False,
        null=False
    )
    fantasy_name = models.CharField(
        max_length=140, blank=True, null=True
    )
    cnpj = models.CharField(
        unique=True,
        max_length=18,
        blank=False,
        null=False,
    )
    position = models.CharField(max_length=20)
    cep = models.CharField(
        max_length=17, blank=True, null=True
    )
    public_place = models.CharField(
        max_length=249, blank=True, null=True
    )
    complement = models.CharField(
        max_length=249, blank=True, null=True
    )
    neighborhood = models.CharField(
        max_length=80, blank=True, null=True
    )
    city = models.CharField(
        max_length=80, blank=True, null=True
    )
    state = models.CharField(
        max_length=80, blank=True, null=True
    )
    number = models.IntegerField(blank=True, null=True)

    phone = models.CharField(
        max_length=17, blank=True, null=True
    )
    segmentation = models.CharField(
        choices=SEGMENTATION_CHOICES,
        null=False,
        blank=False,
        default='0',
        max_length=3,
    )
    approved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.corporate_name
