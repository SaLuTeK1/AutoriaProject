from django_filters import rest_framework as filters


class AdvertFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('car__year', 'lt')
    year_gt = filters.NumberFilter('car__year', 'gt')
    brand = filters.CharFilter('car__brand', 'icontains')
    order = filters.OrderingFilter(
        fields=(
            'id'
        )
    )