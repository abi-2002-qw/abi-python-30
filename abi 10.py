#vanessa albigail alvardo elizalde #
#Solicita un año y determina si es bisiesto
#(divisible entre 4 pero no entre 100, excepto si es divisible entre 400).
#Ejemplo: Entrada: 2024 → Salida: "Es bisiesto".
anio = int(input("escriba el año: "))
bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
print("lo es bisiesto." if bisiesto else "no es bisiesto.")
