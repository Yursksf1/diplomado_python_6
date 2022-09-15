from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print('estoy llamando al index')
    return HttpResponse('<b> hola mundo desde django <b>')

def vista_uno(request):
    return HttpResponse('<h1> hola mundo desde la vista numero uno </h1> <p>esta es una vista nueva </p>')
