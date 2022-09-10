# en python podemos definir funcines con multiples parametros


def suma_dos_terminos(a, b):
    return a + b


def suma_tres_terminos(a, b, c):
    return a + b + c


def suma_dos_terminos(a, b, c=0):
    return a + b + c


resultado = suma_dos_terminos(1, 5)
print('resultado', resultado)

resultado = suma_dos_terminos(1, 5, 10)
print('resultado', resultado)

resultado = suma_tres_terminos(1, 5, 10)
print('resultado', resultado)


def suma_n_terminos(*args, **kwargs):
    suma = 0
    print(args)
    print(kwargs)
    for element in args:
        if type(element) in [int, float]:
            suma = suma + element

    for key, element in kwargs.items():
        if type(element) in [int, float]:
            suma = suma + element
    return suma


resultado = suma_n_terminos(1, 5, 10, 12, 8)
print('resultado', resultado)


resultado = suma_n_terminos(0, 'esto es un numero', 11, uno=1, dos=2, tres=3, diez=10, nombre='yurley')
print('resultado', resultado)


# funciones como variables en python
def suma(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

def multiply(*args, **kwargs):
    result = 1
    for element in args:
        result = result * element

    for element in kwargs.values():
        result = result * element
    return result

calculadora = {
    'suma': suma,
    'multiply': multiply
}

terminos = {
    'valor_1': 1,
    'valor_2': 2,
    'valor_3': 3,
    'valor_4': 4,
    'valor_5': 5,
}
operacion = 'multiply'

resultado = calculadora[operacion](**terminos)
print('resultado', resultado)


# Ejercicios.
'''
1) Definir una lista que sera enviada a una funcion. 
    en navidad los niños buenos reciben sus regalos, por lo tanto envian una lista 
    papa noel.

    la funcion debe recibir 2 parametros
    lista de niños buenos, y lista de niño que se portaron mal
    tambien si el niño se porto bien recibira el regalo esperado. 



'''