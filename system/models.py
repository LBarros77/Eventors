from django.db import models

SEGMENTATION_CHOICES = (
    ('0', 'Sem Segmento'),
    ('1', 'Informática'),
    ('2', 'Eletro'),
    ('3', 'Materiais de Construção'),
    ('4', 'Veterinário'),
    ('5', 'Varejo Alimentar'),
    ('6', 'Farma')
)

OPT_IN_CHOICES = (
    ('0', 'Sim'),
    ('1', 'Não')
)

CATEGORY_CHOICES = (
    ('0', 'Visitente'),
    ('1', 'Expositor'),
    ('2', 'Apoio')
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

# Event
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


# Question
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

# Pessoas
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

# Empresas
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

# Inscrição
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

# CheckIn
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
        
#Sorteio
class RafflePrizes(BaseModel):
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE
    )