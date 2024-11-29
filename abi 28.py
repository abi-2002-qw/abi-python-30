#vanessa abigail alvarado #
#Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.
#Ejemplo: Entrada: 5 → Salida: 5 x 1 = 5, ..., 5 x 10 = 50.
numero = int(input("Introduce un número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
