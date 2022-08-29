print("Vamos a calcular el Perimetro, Area y Volumen de un Circulo :")
Radio= float(input("Ingrese el Radio del circulo:"))
Pi= 3.1416
Perimetro = 2 * Pi * Radio 
Area = Pi * Radio ** 2
Volumen= 4/3 * Pi * Radio ** 3
print("Vamos hallar el Perimetro de un Circulo.")
print("Recuerda el Perimetro de un Circulo es la 2*Pi*Radio")
 
print('el perimetro es de: {} Unidades Lineales'.format(Perimetro))

 
print("Ahora vamos hallar el Area del Circulo")
print("Recuerda el Area de un Circulo es Pi*Radio al cuadrado")
print('el Area es de un Circulo: {} Unidades Cuadradas'.format(Area))

print(" Calculemos ahora el volumen de una Esfera")
print("Recuerda el Volumen de una Esfera es 4/3 por Pi por Radio al cubo")
print('el Volumen de una Esfera es : {} Unidades Cubicas'.format(Volumen))
