from django_filters import rest_framework as filters


class AdvertFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('car__year', 'lt')
    year_gt = filters.NumberFilter('car__year', 'gt')

    brand = filters.CharFilter('car__brand', 'icontains')

    region = filters.CharFilter('region', 'icontains')

    price_gt = filters.NumberFilter('car__price', 'gt')
    price_lt = filters.NumberFilter('car__price', 'lt')

    order = filters.OrderingFilter(
        fields=(
            'id'
        )
    )