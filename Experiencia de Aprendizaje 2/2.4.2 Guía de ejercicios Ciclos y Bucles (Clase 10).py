#EJERCICIO 1 - Solicitud de bultos y entrega de precios "FOR, TRY-ECXEPT, IF-ELSE"

livianos = 0
normales = 0

bultos = int(input("Ingrese la cantidad de bultos: "))
for i in range(bultos):

    try:
        peso = float(input(f"Ingrese el peso del bulto {i+1} (en kilos): "))

        if 1 <= peso <= 5:
            livianos += 1
        else:
            normales += 1

        valor_livianos = livianos * 1000
        valor_normales = normales * 2000
        total = valor_livianos + valor_normales

    except ValueError: print("Error: Ingrese un valor numérico válido para el peso.")

print(f"{livianos} bultos ${valor_livianos}")
print(f"{normales} bultos ${valor_normales}")
print(f"Valor total a pagar: ${total}")