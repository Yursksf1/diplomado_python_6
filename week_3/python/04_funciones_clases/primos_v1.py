# este archivo vamos a ver el performance de los algoritmos para hallar numeros primos.

'''
1) recorrer todo los numeros del 1, al numero y validamos el modulo
'''

def is_prime_v1(n):
    validacion = True
    for i in range(2, n):
        if n % i == 0:
            validacion = False
    return validacion

# print(is_prime(31))
# print(is_prime(30))


'''
2) recorrer todo los numeros hasta llegar al que lo divide y si es asi se detiene la funcion y retorna false  
'''

def is_prime(n):
    validacion = True
    for i in range(2, n):
        if n % i == 0:
            validacion = False
            return validacion
    return validacion

# print(is_prime(31))
# print(is_prime(30))


'''
3) en caso de ser primo, no recorremos todos, sino la mitad,   
'''

def is_prime(n):
    validacion = True
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            validacion = False
            return validacion
    return validacion

# print(is_prime(30))
# print(is_prime(31))

'''
4) en caso de ser primo, no recorremos todos, sino la raiz cuadrada.   
'''

def is_prime(n):
    validacion = True
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            validacion = False
            return validacion
    return validacion

# print(is_prime(100))
# print(is_prime(101))


'''
5) en caso de ser primo, no recorremos todos, sino la raiz cuadrada.   
    hacer una bolsa de primos
'''

bolsa_de_primos = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]


def is_prime_v5(n):
    validacion = True
    for i in bolsa_de_primos:
        if i <= n**(1/2):
            if n % i == 0:
                validacion = False
                return validacion
        else:
            return validacion

import time
inicio = time.time()

for i in range(2, 9000):
    if is_prime_v5(i):
        pass
        # print(i)
fin = time.time()
print(fin-inicio)


inicio = time.time()

for i in range(2, 9000):
    if is_prime_v1(i):
        pass
        # print(i)
fin = time.time()
print(fin-inicio)
