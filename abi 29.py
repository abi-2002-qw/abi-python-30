#vanessa abigail alvardo elizalde #
#Imprime todos los números pares entre 1 y 20.
#Salida esperada: 2, 4, 6, ..., 20.
#
for i in range(1, 21):
    if i % 2 == 0:
        if i < 20:
            print(i, end=", ")
        else:
            print(i)
