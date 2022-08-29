# Rectangulo
base = int(input('ingrese la longitud de la base: '))
altura = 3
ancho = 2
print('dimensiones: base: {}, altura: {}, ancho: {}'.format(base, altura, ancho))

# perimetro
print('calcluando el perimetro...')
perimetro = 2 * base + 2 * altura
print('el perimetro es de: {}'.format(perimetro))


# Area
print('calcluando el area...')
area = base * altura
print('el area es de: {}'.format(area))


# Volumen
print('calcluando el volumen...')
volumen = base * altura * ancho
print('el volumen es de: {}'.format(volumen))
