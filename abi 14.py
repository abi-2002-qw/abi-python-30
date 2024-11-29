#vanessa abigail alvardo elizalde #
#Solicita una calificación numérica y devuelve la letra correspondiente:
#90-100: A. _80-89: B._70-79: C._60-69: D._Menor a 60: F
#
calificacion = float(input("Ingresa tu calificación numérica: "))
#90-100: A. _80-89: B._70-79: C._60-69: D._Menor a 60: F
if 90 <= calificacion <= 100:
    letra = 'A'
elif 80 <= calificacion < 90:
    letra = 'B'
elif 70 <= calificacion < 80:
    letra = 'C'
elif 60 <= calificacion < 70:
    letra = 'D'
elif calificacion < 60:
    letra = 'F'
else:
    letra = 'fuera de rango'

# Mostrar el resultado
print(f"la letra correspondiente es: {letra}")
