from django.http import HttpResponse
from django.shortcuts import render
from .queries import QueryDataForVisual
from .models import OnlineShopperTable
def Home(request):
    rev_data = QueryDataForVisual()
    all_revenue = rev_data.QueryRevenue()
    Rev_d = OnlineShopperTable.objects.all()#values('Revenue')
    return render(request, 'home.html',{'Revenues', Rev_d})

# def product_detail_view(request):
#     return