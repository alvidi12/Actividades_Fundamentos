#1. Ordenar los bloques de código.
sw = 1
puntos = 100000
while sw==1:
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print(f"Tiene un total de {puntos} puntos")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 2:
                if(puntos>=10000):
                    print("Seleccione el producto a canjear")
                    print("1.-  Gift Card de $10.000, valor de 10.000 puntos")
                    print("2.-  Secadora de pelo, valor de: 25.000 puntos")
                    print("3.-  Disco duro portátil, valor de: 30.000 puntos")
                    continu = int(input("Seleccione la opción"))
                    if continu==1:
                        puntos = puntos-10000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                    if continu==2:
                        puntos = puntos-25000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                    if continu==3:
                        puntos = puntos-30000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                else:
                    print("No le quedan puntos disponibles")
            if op == 3:
                print("Muchas gracias por ocupar el servicio, adiós")
                sw=0
        else: 
            print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")

#2 Cajero automático
sw = 1
while sw==1:
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print("Tiene un saldo de $500000")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 2:
                print("Transferencia realizada")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 3:
                print("Cierre de sesión exitoso, adiós")
                sw=0
        else: 
            print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")

#3 #Carga Tarjeta Bip
sw = 1
saldo = 0
while sw==1:
    print("1. Ver mi Saldo")
    print("2. Cargar Saldo")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print(f"Tiene un saldo de {saldo}")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 2:
                print("¿Cuánto desea cargar?")
                print("1.-  $1.000")
                print("2.-  $5.000")
                print("3.- $20.000")
                continu = int(input("Seleccione la opción"))
                if continu==1:
                    saldo = saldo+1000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                if continu==2:
                    saldo = saldo+5000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                if continu==3:
                    saldo = saldo+20000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")            
                if op == 3:
                    print("Muchas gracias por ocupar el servicio, adiós")
                    sw=0
            else: 
                print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")
