from django.test import TestCase
from system.models.company import Company


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
			company_name="Company A",
			corporate_name="Company Test",
			fantasy_name="Test",
			cnpj="",
			position="Admin",
			cep="",
			public_place="",
			complement="House",
			neighborhood="neighborhood",
			city="Manchester City",
			state="NY",
			number=38,
			phone="349925476324",
			segmentation=random.choice(SEGMENTATION_CHOICES),
			approved=True
		)

	def test_company_name_company(self):
		self.assertEquals(self.company.company_name, 'Company A')
