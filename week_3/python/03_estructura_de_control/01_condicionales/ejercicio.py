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


"""
+ * - 
de lunes a vierens --> descuento de pasta y arroz 
marte --> no hay descuento
Miercoles --> de descuento frutas y verduras  (20 %)
Jueves --> descuento pollo y carne ( 15 %)
viernes --> descuento de licores y cerverza 
fines de semana --> descuento en pañales 

la compra es de:
producto -- valor base
arroz: 10.000  
carne: 30.000
pollo: 20.000
licor: 59.000
pañales: 50.000
pañitos humedos: 7800
pastas: 15000
mazanas: 5000
pera: 5000
kiwi: 7800
fresa: 4500


- que dia de la semana me conviente hacer las compras. 

teniendo en cuenta los descuentos.
y que si soy cliente frecuente tendre un 5% de descuento.

- cuanto fue el valor total de la compra. 
"""

