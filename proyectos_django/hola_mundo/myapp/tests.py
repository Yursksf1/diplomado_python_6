from django.test import TestCase

# Create your tests here.


def suma(a, b):
    return a+b

def sumaPares(n):
    suma = 0
    for i in range(n+1):
        if i % 2 == 0:
            suma = suma+i
    return suma


assert(suma(1, 1) == 2)
assert(suma(1, 2) == 3)
assert(suma(1, 3) == 4)

assert(sumaPares(10) == 30)
assert(sumaPares(12) == 42)
