
from django.contrib import admin
from django.urls import path, include

from ErpDev import views
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    #url(r'^$',views.Home,name='Home'),
    url(r'^ToDo/$', views.index, name="TodoList")
]
