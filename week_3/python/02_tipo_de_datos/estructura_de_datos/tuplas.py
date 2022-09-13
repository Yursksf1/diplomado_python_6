my_tupla = (1.123123123, 4.31123123, 5.123213123, [])

print(len(my_tupla))
print(my_tupla[0])
print(my_tupla[2])

# iterar
for i in my_tupla:
    print(i)

# errores
# my_tupla.append(5)
# my_tupla.remove(5)

my_tupla[3].append(8)
print(my_tupla)