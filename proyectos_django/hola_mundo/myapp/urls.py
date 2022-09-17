from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

# Django
from django.urls import include, path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.sin_ruta, name="sin_ruta"),
    path('vista_con_texto_v54678', views.vista_con_texto, name="vista_con_texto"),
    path('vista_con_template', views.vista_con_template, name="vista_con_template"),
    path('vista_generica', TemplateView.as_view(template_name='index.html'), name='vista_generica'),

    path('home', TemplateView.as_view(template_name='home.html'))

]