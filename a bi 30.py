#vanessa abigail alvaedo elizalde #
#Imprime los números del 10 al 1 en orden descendente.
#Salida esperada: 10, 9, 8, ..., 1
for i in range(10, 0, -1):
    if i > 1:
        print(i, end=", ")
    else:
        print(i)
