'''
definir un programa en python que pregunte
tu edad y nos diga si eres o no mayor de edad
'''

# respuesta = int(input('cual es tu edad? '))
# if respuesta >= 18:
#     print('Eres mayor de edad')
# else:
#     print('No eres mayor de edad')


'''
definir un programa en python que reciba una mensaje de texto 
y alerte al usario si dentro de esa cadena esta la palabra 'amor'
'''


'''
definir un programa en python que reciba señales (verdad o falso)
P y Q 
y evaluen las siguiente expreciones de logica.

P y Q 
P o Q 
no P y Q 
no P
(P o Q) y (no p)  
'''
p = int(input("ingresa 1 para true o 0 para false: ")) == 1
q = int(input("ingresa 1 para true o 0 para false: ")) == 1

print('p', p)
print('q', q)

print('P y Q es: {}'.format(p and q))
print('P o Q es: {}'.format(p or q))

