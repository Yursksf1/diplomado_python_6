# key: valor


my_diccionary = {
    'key': 'valor',
}

dict_espannol_ingles = {
    'dia': 'day',
    'bueno': 'good',
    'lunes': 'monday',
    'martes': 'tuesday'
}

print(dict_espannol_ingles['dia'])
print(dict_espannol_ingles['bueno'])
print(dict_espannol_ingles['martes'])

print(len(dict_espannol_ingles))

# iterar
for key, value in dict_espannol_ingles.items():
    print(key, value)


for key in dict_espannol_ingles:
    print(key, dict_espannol_ingles[key])


for value in dict_espannol_ingles.values():
    print(value)

dict_espannol_ingles['m'] = 'miercoles'
dict_espannol_ingles['dia'] = 'sabado'
dict_espannol_ingles['mes'] = 'enero'
dict_espannol_ingles['anno'] = '2022'

print('dict_espannol_ingles', dict_espannol_ingles)

# tener
print(dict_espannol_ingles['mes'])
# print(dict_espannol_ingles['meses'])
print(dict_espannol_ingles.get('mes'))
print(dict_espannol_ingles.get('meses'))

print(help(dict))