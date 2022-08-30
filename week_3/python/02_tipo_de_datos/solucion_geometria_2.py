# Triangulo
base = int(input('Cuanto mide la base del triángulo: '))
altura = int(input('Cuánto mide la altura del triángulo: '))
profundidad = int(input('Cuánto mide la profundidad de tu triángulo: '))

lado = (altura**2 + (base/2)** 2)**(1/2)
perimetro = base + lado + lado
area = (base * altura) / 2
volumen = area * profundidad

print('\n')
print(f'el perimetro del triángulo es {perimetro}')
print(f'el area del triángulo es {area}')
print(f'el volumen del triángulo es {volumen}')
