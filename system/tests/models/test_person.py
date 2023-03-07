from django.test import TestCase
from system.models.person import Person


OPT_IN_CHOICES = (
    ('0', 'Sim'),
    ('1', 'Não')
)

CATEGORY_CHOICES = (
    ('0', 'Visitente'),
    ('1', 'Expositor'),
    ('2', 'Apoio')
)

NAME = 'Test'
NAME_CRACHA = 'Test Cracha'
CATEGORY = random.choice(CATEGORY_CHOICES)
CELL_PHONE = '869923356312'
CPF = '23467532408'
EMAIL = 'test@company.com'
PHONE = '43284325'
ROLE = 'role'
COMPANY = 'Company Test'
OPT_IN = random.choice(OPT_IN_CHOICES)


class PersonTestCase(TestCase):
	def setUp(self):
		self.name = NAME
		self.name_cracha = NAME_CRACHA
		self.category = CATEGORY
		self.cell_phone = CELL_PHONE
		self.cpf = CPF
		self.email = EMAIL
		self.phone = PHONE
		self.role = ROLE
		self.company = COMPANY
		self.opt_in = OPT_IN

	def test_get_person(self):
		#

	def test_str_person(self):
		self.assertEquals(str(self.name), Person.objects.get(name=self.name))