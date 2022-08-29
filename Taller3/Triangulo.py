print("Bamos hallar el Perimetro , Area y Volumen de un Triangulo.")
print("Bamos hallar el Perimetro de un Triangulo.")
print("Recuerda el Perimetro de un Triangulo es la suma de todos sus lados")
Altura = float(input("Ingrese la Altura del Triangulo"))
LBase = float(input("ingresa la longitud de la base  del triangulo : ") )
LI = float(input("ingresa la longitud del ladoIzquierdo del triangulo : ") )
LD = float(input("ingresa la longitud del ladoDerecho  del triangulo : ") )

Perimetro = LBase + LI + LD
Area= (LBase * Altura) / 2
Base = LBase * Altura
Volumen= ((Base) * Altura) / 3  
print('el perimetro es de: {}'.format(Perimetro))

 
print("Ahora vamos hallar el Area del Triangulo")
print("Recuerda el Area de un Triangulo es Base por la altura ,dividido en 2")
print('el Area es de: {}'.format(Area))

print(" Calculemos ahora el volumen de un Triangulo")
print("Recuerda el Volumen de un Triangulo es el area de la Base por la altura dividido en 3")
print('el Volumen de un Triangulo es : {}'.format(Volumen))