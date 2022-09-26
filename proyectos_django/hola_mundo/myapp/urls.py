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

    path('home', TemplateView.as_view(template_name='home.html')),
    path('ejemplo_numeros', views.ejemplo_numeros),
    path('numeros_1_100', views.numeros_1_100, name="numeros_1_100"),
    path('numeros_pares', views.numeros_pares, name="numeros_pares"),

    path('rec_1', TemplateView.as_view(template_name='rec_1.html'), name='rec_1'),
    path('rec_2', TemplateView.as_view(template_name='rec_2.html'), name='rec_2'),
    path('rec_3', views.rec_3, name='rec_3'),

]