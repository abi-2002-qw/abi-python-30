#vanessa abigail alvardo elizalde #
#Solicita el día y mes de nacimiento y determina el signo zodiacal del usuario.
#Ejemplo: Entrada: 22, marzo → Salida: "Tu signo es Aries
#Aries: 21 de marzo - 19 de abril
#Tauro: 20 de abril - 20 de mayo
#Géminis: 21 de mayo - 20 de junio
#Cáncer: 21 de junio - 22 de julio
#Leo: 23 de julio - 22 de agosto
#Virgo: 23 de agosto - 22 de septiembre
#Libra: 23 de septiembre - 22 de octubre
#Escorpio: 23 de octubre - 21 de noviembre
#Sagitario: 22 de noviembre - 21 de diciembre
#Capricornio: 22 de diciembre - 19 de enero
#Acuario: 20 de enero - 18 de febrero
#Piscis: 19 de febrero - 20 de marzo

def obtener_signo_zodiacal(dia, mes):#año no vamos a necesitar #
     ##
    if (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
        return "Aries"
    elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
        return "Tauro"
    elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20):
        return "Géminis"
    elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22):
        return "Cáncer"
    elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
        return "Leo"
    elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22):
        return "Virgo"
    elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22):
        return "Libra"
    elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21):
        return "Escorpio"
    elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21):
        return "Sagitario"
    elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19):
        return "Capricornio"
    elif (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18):
        return "Acuario"
    elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20):
        return "Piscis"
dia = int(input("Ingresa tu día de nacimiento: "))
mes = input("Ingresa tu mes de nacimiento (en letras minusculas): ").lower()
signo = obtener_signo_zodiacal(dia, mes)#asignar el zodiaco#
print(f"Tu signo es {signo}.")
