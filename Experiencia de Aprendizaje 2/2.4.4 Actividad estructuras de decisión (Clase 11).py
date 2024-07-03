#Venta de pasajes:
try:
    pasajes = int(input("Ingrese la cantidad de pasajes que desea vender: "))
    totalIngresos = 0
    for i in range(pasajes):
        try:
            valorPasaje = float(input(f"Ingrese el precio del pasaje {i + 1}: "))
            totalIngresos += valorPasaje
        except ValueError:
            print("Debes ingresar un valor válido.")
            break
    else:
        print(f"Total de ingresos por la venta de pasajes: ${totalIngresos:.0f}")
except ValueError:
    print("Error: Ingresar un número válido.")
    