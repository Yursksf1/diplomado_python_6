print('rango', range(5, 10))
for i in range(5, 10):
    print(i)

string = 'hola mundo'
for i in string:
    print(i)


lista = [1,2,3,5,11,21, 0]
for i in lista:
    print(i)

# imprimir numeros pares hasta 100
for i in range(101):
    is_pair = i % 2 == 0
    if is_pair:
        print(i)

diccionario = {
    'uno': 1,
    'dos': 2,
    'tres': 3
}

for key, value in diccionario.items():
    print('tenemos de llave: {}'.format(key))
    print('tenemos de valor: {}'.format(value))
    print('\n')

texto = 'esto es un texto'
texto_split = texto.split()
for palabra in texto_split:
    print(palabra)