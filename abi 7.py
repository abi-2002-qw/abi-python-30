#vanessa abigail alvarado elizalde #
#Solicita tres números y determina cuál es el mayor.
#Ejemplo: Entrada: 4, 9, 2 → Salida: "El número mayor es 9".
#num1 = 1
#num2 = 2
#num3 = 3
num1, num2, num3 = map(int, input("ingresa tres números separados por comas: ").split(","))
mayor = max(num1, num2, num3)
print(f"el número mayor es {mayor}.")
