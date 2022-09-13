# while hace una pergunta.
# muentra eso sea real, se va a ejecutar el codigo que le siga...

'''
while bool:
    # your code is here

ejemplo:
i = 10
while i < 100:
    i = i + 1
    print(i)

'''


edad = 15 # es menor de edad porque tiene 15 años y la mayoria de edad es a los 18
is_mayor_de_edad = edad >= 18

while not is_mayor_de_edad:
    print('feliz cumpleaños, tu edad es: {}'.format(edad))
    edad = edad + 1
    is_mayor_de_edad = edad >= 18

print('sali del while ')

while True:
    print('de aca voy a salir rapido')
    break
print('sali de un while imposible de incumplir')


i = 10
while i < 100:
    i = i + 1
    print(i)

i = 10
while True:
    i = i + 1
    print(i)
    if i >= 100:
        break


# Ejercicios:
'''
1) For :
hacer un programa en python que recorra un rango de 50 a 100, 
e imprima los numero impares 
ejemplo
51, 53, 55 ... 99

2) while
hacer un progrma en python que imprima el nombre de el usuario 
y salude cordialmente. 
y no deje de preguntar el nombre hasta que ingrese el 0 
ejemplo
cual es tu nombre? 'yurley'
Hola Yurley
cual es tu nombre? 'Carlos'
Hola Carlos
cual es tu nombre? 0 
chaito.

3) while  
hace un programa en python que reciba de parametro cuanto dinero tengo 
en efectivo.
y me ayude con las compras.
el programa debe restar el dinero hasta que se acabe o sea negativo

ejemplo
- cuanto dinero tenes: 500.000
te voy a ayudar con las compras:
cuanto gataste? 10000
te queda un saldo de: 490.000

cuanto gataste? 100000
te queda un saldo de: 390.000

cuanto gataste? 150000
te queda un saldo de: 240.000
.....

cuanto gataste? 240000
te queda un saldo de: 0

se acabo el dinero vueve a retirar. 

'''