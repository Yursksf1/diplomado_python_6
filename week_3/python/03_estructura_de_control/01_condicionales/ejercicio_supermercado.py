
"""
+ * -
de lunes a viernes --> descuento de pasta y arroz ( 10 %)
marte --> no hay descuento
Miercoles --> de descuento frutas y verduras  (20 %)
Jueves --> descuento pollo y carne ( 15 %)
viernes --> descuento de licores y cerverza (20 %)
fines de semana --> descuento en pañales  (15 %)

la compra es de:
producto -- valor base
arroz: 10.000
carne: 30.000
pollo: 20.000
licor:  59.000
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


print('... Calculando el total de la compra ...')

arroz = 10000
carne = 30000
pollo = 20000
licor = 59000
pañales = 50000
pañitos_humedos = 7800
pastas = 15000
mazanas = 5000
pera = 5000
kiwi = 7800
fresa = 4500
dia_de_la_semana = 'sabado' # ingresar esto con un imput

if dia_de_la_semana == 'lunes':
    arroz = arroz * (1 - 0.1)
    pastas = pastas * (1 - 0.1)

elif dia_de_la_semana == 'martes':
    arroz = arroz * (1 - 0.1)
    pastas = pastas * (1 - 0.1)

elif dia_de_la_semana == 'miercoles':
    arroz = arroz * (1 - 0.1)
    pastas = pastas * (1 - 0.1)
    mazanas = mazanas * (1 - 0.2)
    pera = pera * (1 - 0.2)
    kiwi = kiwi * (1 - 0.2)
    fresa = fresa * (1 - 0.2)

elif dia_de_la_semana == 'jueves':
    arroz = arroz * (1 - 0.1)
    pastas = pastas * (1 - 0.1)
    carne = carne * (1 - 0.15)
    pollo = pollo * (1 - 0.15)

elif dia_de_la_semana == 'viernes':
    arroz = arroz * (1 - 0.1)
    pastas = pastas * (1 - 0.1)
    licor = licor * (1 - 0.2)

else:
    pañales = pañales * (1 - 0.15)
    pañitos_humedos = pañitos_humedos * (1 - 0.15)

total = arroz + carne + pollo + licor + pañales + pañitos_humedos + pastas + mazanas + pera + kiwi + fresa
print('el total sin descuentos es: {}'.format(total))
decuento_cliente_frecuente = total*(0.05)
print('el descuento por cliente frecuente es de 5% es decir: {}'.format(decuento_cliente_frecuente))
valor_total = total - decuento_cliente_frecuente
print('valor final: {}'.format(valor_total))