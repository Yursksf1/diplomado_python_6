from django.shortcuts import render, HttpResponse

# Create your views here.
def numeros_1_100(request):
    html_base = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    {contenido}
    </body>
    </html>
    """

    mensaje_respuesta = ""
    for i in range(1, 101):
        mensaje_respuesta = mensaje_respuesta + '<br>' + str(i)
    print('mensaje_respuesta', mensaje_respuesta)
    return HttpResponse(html_base.format(contenido=mensaje_respuesta))

def numeros_pares(request):
    mensaje_respuesta = ""

    for i in range(1, 202):
        if i % 2 == 0:
            mensaje_respuesta = mensaje_respuesta + '<br>' + str(i)

    for i in range(1, 101):
        mensaje_respuesta = mensaje_respuesta + '<br>' + str(i*2)

    contador = 0
    iterador = 1
    while(contador<100):
        iterador = iterador + 1
        if iterador % 2 == 0:
            contador = contador + 1
            mensaje_respuesta = mensaje_respuesta + '<br>' + str(iterador)

    return HttpResponse(mensaje_respuesta)


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
