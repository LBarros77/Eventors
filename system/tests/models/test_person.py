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

TELEPHONE_PREFIXES = (
	# Southeast
	11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 21, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38,
	# South
	41, 42,	43,	44,	45,	46,	47,	48,	49,	51,	53,	54,	55,
	# midwest
	61, 62, 63, 64, 65, 66, 67, 68,
	# Northeast
	71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89,
	# North
	91, 92, 93, 94, 95, 96, 97, 98, 99
)

class PersonTestCase(TestCase):
	def setUp(self):
		self.person = Person.objects.create(
			name = 'Test',
			name_cracha = 'Test Cracha',
			category = random.choice(CATEGORY_CHOICES),
			cell_phone = '869923356312',
			cpf = '23467532408',
			email = 'test@company.com',
			phone = '43284325',
			role = 'role',
			company = 'Company Test',
			opt_in = random.choice(OPT_IN_CHOICES)
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
		cell_phone = self.person.cell_phone
		if len(cell_phone) >= 8 and len(cell_phone) <= 11:
			size = len(cell_phone)
			if size == 8 or size == 9:
				is_valid = int(cell_phone[0]) > 4 and int(cell_phone[0]) < 10
			is_valid = int(cell_phone[2]) > 4 and int(cell_phone[2]) < 10 and int(cell_phone[:2] in TELEPHONE_PREFIXES)
		else:
			size = 0
			is_valid = False
		self.assertEquals(int(cell_phone), True)
		self.assertEquals(is_valid, True)

	def test_cpf_person(self):
		self.assertEquals(int(cell_phone), True)
		self.assertEquals(len(self.person.cpf), 11)

	def test_email_person(self):
		#

	def test_phone_company(self):
		first_number = int(self.person.phone[0])
		self.assertBoolean(first_number > 1 and first_number < 6)
		self.assertEquals(len(self.person.phone), 8 or 10)

	def test_str_person(self):
		self.assertEquals(str(self.name), Person.objects.get(name=self.name))