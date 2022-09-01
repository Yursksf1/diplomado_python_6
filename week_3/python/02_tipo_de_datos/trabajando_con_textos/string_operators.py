help(str)

# upper
texto = 'hola munDo'
print(texto)
print(texto.upper())

# lower
texto = 'hola MundO'
print(texto)
print(texto.lower())

# capitalize
texto = 'hola mundo'
print(texto)
print(texto.capitalize())

# title
texto = 'hola mundo'
print(texto)
print(texto.title())

# title
texto = 'Hola Mundo'
print(texto)
print(texto.swapcase())


# count
texto = 'hola mundo'
print(texto)
print(texto.count('a'))


# endswith
texto = 'hola mundo'
print(texto)
print(texto.endswith('ndo'))
print(texto.endswith('123'))


# format
texto = 'hola mundo {}'
print(texto)
print(texto.format('feliz'))
texto = 'hola {} mundo'
print(texto)
print(texto.format('feliz'))

# iterar
texto = 'hola mundo'
for w in texto:
    print(w)

# concatenar
texto_1 = 'hola'
texto_2 = 'mundo'
texto_3 = texto_1 + ' ' + texto_2
print(texto_3)

texto_3 = '{} {}'.format(texto_1, texto_2)
print(texto_3)

# index
texto = 'hola mundo'
print(texto)
print(texto.index('a'))

# index
texto = 'hola mundo'
print(texto)
print('la' in texto)
print('may' in texto)
