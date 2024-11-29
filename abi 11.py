#vanessa abigail alvarado elizalde #
#Escribe un programa que solicite una contraseña y valide
#si es correcta (ejemplo: contraseña fija es 12345).la vamos a cambiar por esta (abi2002_ec)
#Ejemplo: Entrada: 12345 → Salida: "Acceso concedido
# Contraseña fija
contraseña_correcta = "abi2002_ec" #contraceña del usuario 
contraseña = input("ingrese su contraseña: ")
#si --- en caso contraio no 
if contraseña == contraseña_correcta:
    print("contraceña correcta")
else:
    print("contraceña incorecta")
