#vanessa abigail alvaedo elizalde #
#Encuentra e imprime todos los números primos entre 1 y 50.
#Salida esperada: 2, 3, 5, 7, ..., 47
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
primos = []

for num in range(1, 51):
    if es_primo(num):
        primos.append(num)
print(", ".join(map(str, primos)))
