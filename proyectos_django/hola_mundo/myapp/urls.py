from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

# Django
from django.urls import include, path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name="home"),
    path('vista_uno', views.vista_uno, name="vista_uno")
]