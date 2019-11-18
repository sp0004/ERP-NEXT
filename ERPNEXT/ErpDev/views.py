from django.http import HttpResponse
from django.shortcuts import render
from .queries import QueryDataForVisual
from .models import OnlineShopperTable
from django.db.models import Count
def Home(request):
    #rev_data = QueryDataForVisual()
    #all_revenue = rev_data.QueryRevenue()

    Rev_True = OnlineShopperTable.objects.all().filter(Revenue = 'TRUE').count()
    Rev_False = OnlineShopperTable.objects.all().filter(Revenue='FALSE').count()
    context = {
        'True_Val':Rev_True,
        'False_Val': Rev_False
    }
    return render(request, 'home.html',context)

# def product_detail_view(request):
#     return