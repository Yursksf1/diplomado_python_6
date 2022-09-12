
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


