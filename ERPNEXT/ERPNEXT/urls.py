
from django.contrib import admin
from django.urls import path, include
from ErpDev import views
from ErpDev.views import Login_view, signup_view,home_view,todo_view
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path



urlpatterns = [

    path('', Login_view, name="Login"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', Login_view, name="tr"),
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name="signup"),

    path('accounts/',Login_view, name="Login-v"),


    path('signup/registration/Login.html',Login_view,name="Login_from_signup"),
    path('Home/',home_view,name="home"),
    path('ToDo/', todo_view, name="TodoList"),
    #url(r'^logout/$', auth_views.logout)
]
