from django.shortcuts import render, HttpResponse

# Create your views here.
def sin_ruta(request):
    print('>>> sin_ruta')
    return HttpResponse('<b style="color: blue "> hola mundo desde django esta es una vista sin ruta definida <b>')

def vista_con_texto(request):
    print('>>> vista_con_texto')
    return HttpResponse('<h1> hola mundo desde la vista, estoy renderisando este mensaje con texto en python no estoy usando un archivo html </p>')

def vista_con_template(request):
    print('>>> vista_con_template')
    template_name = 'vista_desde_views.html'
    return render(request, template_name=template_name)

def ejemplo_numeros(request):
    template_name = 'ejemplo_numeros.html'
    number_1 = int(request.GET.get('number_1'))
    number_2 = int(request.GET.get('number_2'))
    suma = number_1 + number_2

    context = {
        "result": suma
    }
    return render(request, template_name=template_name, context=context)
