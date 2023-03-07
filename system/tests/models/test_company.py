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
		Company.objects.create(
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
		Company.objects.create(
			company_name="Company B",
			corporate_name="Company Test 2",
			fantasy_name="Test 2",
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

	def test_company_is_approved(self):
		#
