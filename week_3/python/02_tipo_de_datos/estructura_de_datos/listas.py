'''
lista = [elementos_1,elementos_2, elementos_3, ... n ]
'''

dias_de_la_semana = [
    'lunes',
    'martes',
    'miercoles'
]

print('dias_de_la_semana {}'.format(dias_de_la_semana))

# agregar elemento:
dias_de_la_semana.append('jueves')
print('dias_de_la_semana {}'.format(dias_de_la_semana))

## recorderis:
# str
validacion = 'amor' in 'todo es mas lindo cuando lo haces con amor'
print('validacion', validacion)

# en listas puedo hacer validaciones con 'in'
validacion_2 = 'lunes' in dias_de_la_semana
print('validacion_2', validacion_2)

print(dias_de_la_semana[0])
print(dias_de_la_semana[3])
# print(dias_de_la_semana[8])
print(dias_de_la_semana[-1])

# longitud de la lista  funcion len
print(len(dias_de_la_semana))

print(type(dias_de_la_semana))
print(help(list))

print(dias_de_la_semana.count('lunes'))

print(dias_de_la_semana.pop())
print(len(dias_de_la_semana))
print(dias_de_la_semana)


print(dias_de_la_semana.remove('lunes'))
print(len(dias_de_la_semana))
print(dias_de_la_semana)



dias_de_la_semana = [
    'lunes',
    'martes',
    'miercoles',
    'jueves',
    'viernes',
    'sabado',
    'domingo'
]
print('dias_de_la_semana', dias_de_la_semana)
dias_de_la_semana.sort()
print('dias_de_la_semana', dias_de_la_semana)

dias_de_la_semana.sort(reverse=True)
print('dias_de_la_semana', dias_de_la_semana)

# iterables.
for element in dias_de_la_semana:
    print(element)
print('fin del ciclo')
print(dias_de_la_semana[2:5])

nueva_lista = [1, 1.2, 'texto', True, ['otra', 'lista'], {}, ()]
