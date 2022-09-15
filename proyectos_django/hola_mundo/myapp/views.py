from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print('estoy llamando al index')
    return HttpResponse('<b> hola mundo <b>')