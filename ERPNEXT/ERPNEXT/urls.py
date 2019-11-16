
from django.contrib import admin
from django.urls import path

from ErpDev import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.Home,name='Home'),
]
