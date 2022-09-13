# funciones en python

# funcion sin parametro y sin retorno
def imprimir():
    print('estoy llamando a esta funcion')

# funcion con parametro y sin retorno
def imprimir_nombre(nombre):
    print("hola {} mucho gusto".format(nombre))

# funcion sin parametro y con retorno
def genera_saludo():
    return "hola, mucho gusto"

# funcion con parametro y con retorno
def generar_saludo_nombre(nombre=None):
    if not nombre:
        return genera_saludo()
    return "hola {} mucho gusto".format(nombre)

imprimir()
imprimir_nombre(nombre='Juan')
saludo = genera_saludo()
print(saludo)
saludo_con_nombre = generar_saludo_nombre('Marcos')
print(saludo_con_nombre)

saludo_sin_nombre = generar_saludo_nombre()
print(saludo_sin_nombre)

valor = imprimir()
print('valor', valor)


def dividir_con_except(a, b):
    try:
        return a/b
    except:
        print('ocurrio un error')
        return 0

def dividir(a, b):
    if b == 0:
        return 'dividir en 0 no es posible'
    return a/b


resultado = dividir(6, 2)
print(resultado)
resultado = dividir(6, 3)
print(resultado)

resultado = dividir(6, 0)
print(resultado)

'''
Ejercicio: 
1) hacer una calculadora en python 
recibe 2 parametros a operar 
def suma(a, b):
    return a + b
    
llamar e imprimir el resultado 
(suma, resta, multoplicacion, division) 
opcional ( potencia, raiz n-esima)

2) solicitar al usuario por consola haciendo uso del imput para ingresar los valores a operar 
 en la calculadora definida en el punto 1
 
3) hace un menu de opciones. 
'''
