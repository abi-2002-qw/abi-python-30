#vanessa abigail alvarado elizalde #
#Solicita dos números y una operación (+, -, *, /)
#y realiza el cálculocorrespondiente.
#Ejemplo: Entrada: 3, 2, '+' → Salida: "Resultado: 5".
#
# utilizamos float (input())
num1 = float(input("primer número: "))
num2 = float(input("segundo número: "))
operacion = input("que operacion deseas (+, -, *, /): ")
resultado = None
if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2 if num2 != 0 else "/ por cero"
print(f"resultado: {resultado}")
