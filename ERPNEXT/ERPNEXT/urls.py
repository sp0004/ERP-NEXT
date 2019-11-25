
from django.contrib import admin
from django.urls import path, include
from ErpDev import views
from ErpDev.views import Login_view, signup_view,home_view,todo_view,Dashboard_view
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path



urlpatterns = [
    path('', auth_views.LoginView.as_view(), name="Login"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name="signup"),
    path('signup/registration/Login.html',Login_view,name="Login_from_signup"),
    path('Home/',home_view,name="home"),
    path('accounts/login/Home/',home_view,name="home"),
    path('ToDo/', todo_view, name="TodoList"),
    path('Dashboard/',Dashboard_view,name="Dashboard")
]
