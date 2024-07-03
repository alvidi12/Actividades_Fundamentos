#Menú de opciones para pago de cupo de la tarjeta de crédito.

saldo_tarjeta = 100000
while True:
    print("\nMenú de opciones:\n1. Pago de Tarjeta de Créditon\n2. Simulación de Compras\n3. Salir")
    op = input("Seleccione una de las opciones (1 , 2 , 3): ")

    if op == "1":   #Pago de tarjeta de credito.
        try:
            pago = float(input("Ingrese el monto a pagar: "))
            if pago >= 0 and pago <= saldo_tarjeta:
                saldo_tarjeta -= pago
                print(f"Pago realizado. Su saldo actual es de ${saldo_tarjeta:.2f}")
            else:
                print("Error: El monto ingresado no es válido.")
        except ValueError:
            print("Error: Debes ingresar un valor válido.")

    elif op == "2": #Simulación de compras
        try:
            while True:
                compra = float(input("Ingrese el monto de la compra: "))
                if compra == 0:
                    break
                elif compra >= 0:
                    saldo_tarjeta -= compra
                    print(f"Compra realizada. Su saldo actual es de ${saldo_tarjeta:.0f}")
                else:
                    print("Error: El monto de la compra no es válido.")
        except ValueError:
            print("Error: Ingrese un valor válido.")

    elif op == "3": #Salir
        print("Gracias por su apreciado tiempo")
        break

    else:
        print("Error de ingreso de datos.")