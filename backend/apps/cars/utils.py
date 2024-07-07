from django.http import JsonResponse

from .choises import CAR_MODELS, BrandChoices, CarChoices


def get_models(request):
    brand = request.GET.get('brand')
    models = CAR_MODELS.get(brand, [])
    return JsonResponse(models, safe=False)


def get_brands(request):
    brands = [brand.value for brand in BrandChoices]
    return JsonResponse(brands, safe=False)


def get_body_types(request):
    bodies = [body.value for body in CarChoices]
    return JsonResponse(bodies, safe=False)