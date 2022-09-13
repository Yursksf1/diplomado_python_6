
def es_primo(n):
    validation = True
    for j in range(2, n):
        if n % j == 0:
            validation = False
            return validation

    return validation

contador = 0
for i in range(2, 100):
    if es_primo(i):
        contador = contador + 1
        print(contador, i)

numeros = 0
contador = 0
while contador < 100:
    numeros = numeros + 1
    if es_primo(numeros):
        contador = contador + 1
        print(numeros)


