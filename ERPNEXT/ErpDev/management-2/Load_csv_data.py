from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand

from ERPNEXT.ErpDev.models import OnlineShopperTable

# Overloading the command operator
class Command(BaseCommand):
    def handle(self,*args,**options):
        if (OnlineShopperTable.objects.exists()):
            print('Data already inserted')
            return
        print('Inserting Value in table')
        csv = open('./online_shoppers_intention.csv')
        for eachrow in DictReader(csv):
            obj = OnlineShopperTable()
            obj.Administrative = eachrow['Administrative']
            obj.Administrative_Duration = eachrow['Administrative_Duration']
            obj.Informational = eachrow['Informational']
            obj.Informational_Duration = eachrow['Informational_Duration']
            obj.ProductRelated = eachrow['ProductRelated']
            obj.ProductRelated_Duration = eachrow['ProductRelated_Duration']
            obj.BounceRates = eachrow['BounceRates']
            obj.ExitRates = eachrow['ExitRates']
            obj.PageValues = eachrow['PageValues']
            obj.SpecialDay = eachrow['SpecialDay']
            obj.Visitor_type = eachrow['Visitor_type']
            obj.Region = eachrow['Region']
            obj.Browser = eachrow['Browser']
            obj.Weekend = eachrow['Weekend']
            obj.OperatingSystems = eachrow['OperatingSystems']
            obj.Month = eachrow['Month']
            obj.TrafficType = eachrow['TrafficType']
            obj.Revenue = eachrow['Revenue']
            obj.save()
