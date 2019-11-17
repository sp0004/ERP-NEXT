from ErpDev.models import OnlineShopperTable

class QueryDataForVisual:
    def QueryRevenue(self):
        Revenue = OnlineShopperTable.objects.raw('SELECT Revenue from erpdev_onlineshoppertable;')
        # Revenue_False = OnlineShopperTable.objects.raw('select count(Revenue) from erpdev_onlineshoppertable where '
        #                                                'Revenue = "FALSE"')
        # Revenue_True = OnlineShopperTable.objects.raw('select count(Revenue) from erpdev_onlineshoppertable where '
        #                                               'Revenue = "TRUE"')
        return Revenue