from django.test import TestCase
from system.models.company import Company
from .te_person import TELEPHONE_PREFIXES

SEGMENTATION_CHOICES = (
    ('0', 'Sem Segmento'),
    ('1', 'Informática'),
    ('2', 'Eletro'),
    ('3', 'Materiais de Construção'),
    ('4', 'Veterinário'),
    ('5', 'Varejo Alimentar'),
    ('6', 'Farma')
)

class CompanyTestCase(TestCase):
	def setUp(self):
		self.company = Company.objects.create(
			company_name = 'Company A',
			corporate_name = 'Company Test',
			fantasy_name = 'Test',
			cnpj = '52998224725',
			position = 'Admin',
			cep = '56180000',
			public_place = 'Lugar público',
			complement = 'House',
			neighborhood = 'Bairro',
			city = 'Cidade',
			state = 'PE',
			number = 38,
			phone = '349925476324',
			segmentation = random.choice(SEGMENTATION_CHOICES),
			approved = True
		)

	def test_company_name_company(self):
		self.assertEquals(self.company.company_name, 'Company A')

	def test_corporate_name_company(self):
		self.assertEquals(self.company.company_name, 'Company Test')

	def test_fantasy_name_company(self):
		self.assertEquals(self.company.company_name, 'Test')

	def test_cpf_company(self):
		cpf = self.person.cpf
		digits['first_digit'] = cpf[:-2] if len(cpf) == 11 else 0
		digits['second_digit'] = cpf[:-1] if len(cpf) == 11 else 0
		is_valid = digits.first_digit != 0 and digits.second_digit != 0
		for i = 0; i < 8; i++:
			for int[number] in digit.second_digit:
				if number == i:
					count++
					if count == 6:
						is_valid = False
						break
				count = 0
		if is_valid:
			for digit in digits.values():
				verify_first_digit = 0
				count = len(digit)
				for int(number) in digit:
					verify_first_digit += number * count
					count--
				verify_first_digit = (verify_first_digit * 10) % 11
				if len(digit) == 9 and verify_first_digit == cpf[9]:
					is_valid = True
				is_valid = is_valid and len(digit) == 10 and verify_first_digit == cpf[10]
		self.assertBoolean(is_valid)

	def test_position_company(self):
		self.assertEquals(self.company.position, 'Admin')

	def test_cep_company(self):
		try:
			import requests
			get_cep = requests.get('https://viacep.com.br/ws/56180000/json/')
		except:
			get_cep = {'cep': '0'}
		self.assertEquals(get_cep['cep'], '56180000')

	def test_public_place_company(self):
		self.assertEquals(self.company.public_place, 'Lugar público')

	def test_complament_company(self):
		self.assertEquals(self.company.complement, 'Casa')

	def test_neightbordhood_company(self):
		self.assertEquals(self.company.neighborhood, 'Bairro')

	def test_city_company(self):
		self.assertEquals(self.company.city, 'Cidade')

	def test_state_company(self):
		self.assertEquals(self.company.state, 'PE')

	def test_number_company(self):
		self.assertEquals(self.company.number, 38)

	def test_phone_company(self):
		first_number = int(self.person.phone[0])
		self.assertEquals(len(self.person.phone), 8 or 10)
		self.assertBoolean(first_number > 1 and first_number < 6)
		self.assertBoolean(int(self.person.phone[:3]) in TELEPHONE_PREFIXES)

	def test_segmentation_company(self):
		is_valid = self.company.segmentation in SEGMENTATION_CHOICES
		self.assertBoolean(is_valid, True)

	def test_aproved_company(self):
		self.assertBoolean(self.company.approved)