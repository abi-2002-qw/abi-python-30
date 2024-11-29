#vanessa abigail alvardo elizalde #
#Calcula el factorial de un número ingresado por el usuario (n!).
#Ejemplo: Entrada: 5 → Salida: 120
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
numero = int(input("introduce un número : "))
resultado = factorial(numero)
print(f"el factorial de {numero} es: {resultado}")
