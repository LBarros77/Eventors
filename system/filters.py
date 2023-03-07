import django_filters
from system.models.company import Company


class CompanyFilter(django_filters.FilterSet):
    cnpj = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Company
        fields = ['cnpj']
