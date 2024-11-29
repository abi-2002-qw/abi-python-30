#vanessa abigail alvarado elizalde ##
#Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine
#el número. Usa if para verificar si acertó o no.
#Ejemplo: Entrada: 5 → Salida: "¡Felicidades, acertaste!" o "Intenta de nuevo.".
import random
numero_aleatorio = random.randint(1, 10)#1-10#
try:
    adivinanza = int(input("vamos a jugar a adivina. escribe un numero 1 y 10: "))
   #if#
    if adivinanza == numero_aleatorio:
        print("¡Felicidades acertaste!")
    else:
        print("intenta de nuevo. El número era:", numero_aleatorio)
except ValueError:
    print("ingresa un número válido")
