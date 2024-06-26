from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('signin', views.signin, name = 'signin'),
  path('signout', views.signout, name = 'signout'),
  path('endpage', views.endpage, name='endpage'),
  path('activate/<uidb64>/<token>', views.activate, name='activate')
]