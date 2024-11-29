#vanessa abigail alvarado elizade #
#Imprime todos los números pares entre 1 y 20.
#Salida esperada: 2, 4, 6, ..., 20.
# Imprimir los números pares entre 1 y 20
for i in range(1, 21):
    if i % 2 == 0:  
        print(i, end=", " if i < 20 else "")  #<pares #
