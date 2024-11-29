#vanessa abigail alvardo elizalde #
#Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. Escribe un programa que calcule el monto final.
#Ejemplo: Entrada: $120 → Salida: "Monto final: $96".

total = float(input("ingrese el total de la compra: $"))
monto_final = total * 0.8 if total > 100 else total
print(f"total a pagar: ${monto_final:.2f}")
