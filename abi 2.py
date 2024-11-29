#vanessa abigail alvarado elizalde #
#o Solicita al usuario un número y determina si es positivo, negativo o cero.
#o Ejemplo: Entrada: -3 → Salida: "Es un número negativo".

numero = float(input("Ingresa un número: "))
# 
if numero > 0:
    print("Es un número positivo")
elif numero < 0:
    print("Es un número negativo")
else: # en caso contrario 0 #
    print("cero.")#como ultima opcion #
