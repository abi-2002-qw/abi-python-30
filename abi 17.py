#vanessa abigail alvarado elizalde #
#Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.

numero = int(input("introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i#*#
    print(f"{numero} x {i} = {resultado}")
