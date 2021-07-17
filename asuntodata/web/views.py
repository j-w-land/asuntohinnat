from django.http import JsonResponse
from django.shortcuts import render
from web.models import Price
from django.core import serializers
from web.services.PXWeb import get_prices_by_zip


def dashboard_with_pivot(request):
    data = get_prices_by_zip(['53850'])
    # print("DATA::")
   # print(data)
    return render(request, '../templates/charts/dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Price.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
