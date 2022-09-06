# Simular cajero automático
Persona = input("Ingrese su nombre: ")
print("\nBuen día {}".format(Persona), "Soy su cajero automático y tengo el gusto de atenderlo\n")

Options = int(input('''Seleccione la opción que desea realizar: 
1. Retirar dinero
2. Consignar dinero
3. Pago de facturas
---> '''))

if Options == 1:
    Retiro = int(input("Bienvenido a la opción de retiro...\n\nIndiqueme que tipo de retiro desea hacer por favor\n1. Retiro desde nequi\n2. Retiro por medio de tarjeta de credito\n---> "))
    if Retiro == 1:
        Nequi = int(input("Ingrese su número de nequi\n---> "))
        if type(Nequi) == int:
            Monto = int(input("Ahora ingrese el monto que desea retirar (Sin puntos)\n---> $ "))
            if type(Monto) == int:
                COP = int(Retiro/1000)
                Denominacion = [100, 50, 20, 10]
                resto = COP
                for i in range (len(Denominacion)):
                        b = resto//Denominacion[i]
                        if b>0:
                            print (b, "billetes de ", Denominacion[i], "pesos colombianos")
                            resto%=Denominacion[i]