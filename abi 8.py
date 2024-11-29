#vanessa abigail alvarado elizalde #
#Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+).
#Ejemplo: Entrada: 15 → Salida: "Eres adolescente"#
#
# nino - adolescente
edad = int(input("cuantos años tienes: "))
# si no 
if 0 <= edad <= 12:#niño
    print("eres  un niño")
elif 13 <= edad <= 17:#adolescente
    print("ya eres adolescente")
elif edad >= 18:#mayor de edad 
    print("eres adulto")
else:
    print("edad fuera de rango")

