from django.urls import path
from django.contrib.auth import views as auth_views
#from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('', views.index, name='index')
]
