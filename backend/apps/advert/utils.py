from django.http import JsonResponse

from .choises import RegionChoices


def get_region(request):
    regions = [region.value for region in RegionChoices]
    return JsonResponse(regions, safe=False)