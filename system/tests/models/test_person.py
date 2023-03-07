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
		self.person = Person.objects.create(
			name = NAME,
			name_cracha = NAME_CRACHA,
			category = CATEGORY,
			cell_phone = CELL_PHONE,
			cpf = CPF,
			email = EMAIL,
			phone = PHONE,
			role = ROLE,
			company = COMPANY,
			opt_in = OPT_IN
		)

	def test_name_person(self):
		self.assertEquals(self.person.name, NAME)
	
	def test_name_cracha_person(self):
		self.assertEquals(self.person.name_cracha, NAME_CRACHA)

	def test_category_person(self):
		for category in CATEGORY_CHOICES:
			if self.category == category:
				self.assertEquals(self.person.category, self.category)

	def test_cell_phone_company(self):
		# Identify...

	def test_str_person(self):
		self.assertEquals(str(self.name), Person.objects.get(name=self.name))