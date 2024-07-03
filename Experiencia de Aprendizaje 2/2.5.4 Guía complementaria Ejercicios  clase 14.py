#Ejercicio 1
patio = False
sala = False
pasillo = False
jardin = False
while True:
    print("1.- Enceder/Apagar luces Patio (Alternado)")
    print("2.- Enceder/Apagar luces Sala (Alternado)")
    print("3.- Enceder/Apagar luces Pasillo (Alternado)")
    print("4.- Enceder/Apagar luces Jardín (Alternado)")
    print("5.- Enceder todo (Alternado)")
    print("6.- Apagar todo (Alternado)")
    print("7.- Salir del sistema")
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except:
        opcion = 0
 
    if opcion == 1:
        patio = not patio
        print("El patio está ", "encendido" if patio  else "apagado")
 
    elif opcion == 2:
        sala = not sala
        print("La sala está ", "encendida" if  sala else "apagada")
 
    elif opcion == 3:
        pasillo = not pasillo
        print("El pasillo está ","encendida" if pasillo  else "apagado")
 
    elif opcion == 4:
        jardin = not jardin
        print("El jardín está ", "encendida" if jardin  else "apagado")
 
    elif opcion == 5:
        patio = True
        sala = True
        pasillo = True
        jardin = True   
        print("Se han encendido todas las luces")
 
    elif opcion == 6:
        patio = False
        sala = False
        pasillo = False
        jardin = False      
        print("Se han apagado todas las luces")
 
    elif opcion == 7:
        print("Hasta pronto...")
        break
    else:
        print("Opción no válida")

#Ejercicio 2
import random
opcion = 0
pago = 100000
while True:
    print("***************Menu*******************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except:
        opcion = 0
 
    if opcion == 1:
        numero =input("Ingrese número de tarjeta de crédito: ")
        nombre = input("Ingrese nombre titular: ")
        mes = input("Ingrese mes de vencimiento: ")
        anio = input("Ingrese año vencimiento: ")
        print("Detalle compra")
        print(f"Costo de la compra: {pago}")
        print("Número de tarjeta: ", numero)
        print("Nombre del titular: ", nombre)
        print(f"Mes y año: {mes}/{anio}")
        break
 
    elif opcion == 2:
        usuario = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")
        print("")
        print("Detalle compra")
        print(f"Costo de la compra: {pago}")        
        print("Usuario: ",usuario)
        print("Password: ********")   
        break
 
    elif opcion == 3:
        numero_orden = random.randint(10000,99999)
        print("Detalle compra")
        print("Código referencia: ",numero_orden)
        print(f"Costo de la compra: {pago}")        
        print("Nombre Destinatario: Dulce Capricho S.A.")
        print("Número de cuenta: 79.548.642-0")   
        print("Banco: Banco Internacional")    
        print("Correo: pago@capricho.com")       
        break 

    elif opcion == 4:
        print("Pago cancelado")
    elif opcion == 5:
        print("Hasta pronto...")
        break
    else:
        print("Opción no válida")
print ("Muchas gracias por su compra")

#Ejercicio 3
print("Calculadora geométrica")  
while True:  
    print("***********Menu************")  
    print("1. Calcular Perímetro")  
    print("2. Calcular Área")  
    print("3. Salir")  
    opcion = int(input("Elija una opción: "))
 
    if opcion == 1:  
        while True:  
            print("Calcular Perímetro")  
            print("1. Para Círculo")  
            print("2. Para Rectángulo")  
            print("3. Para Cuadrado")  
            print("4. Volver menu principal")  
            opcion2 = int(input("Elija una opción: "))  
            if opcion2 == 1:  
                radio = int(input("Ingrese radio del circulo: "))              
                perimetro = 2 * 3.14 * radio  
                print("Perímetro del Circulo: ", perimetro)  
            elif opcion2 == 2:  
                altura = int(input("Ingrese altura del Rectángulo: "))  
                ancho = int(input("Ingrese ancho del Rectángulo: "))  
                perimetro = 2 * (altura + ancho)  
                print("Perímetro del Rectángulo: ", perimetro)  
            elif opcion2 == 3:  
                lado = int(input("Ingrese lado del Cuadrado: "))  
                perimetro = 4 * lado  
                print("Perimetro del cuadrado: ", perimetro)              
            elif opcion2 == 4:  
                break         
            else:  
                print("Elección inválida.")  
    
    elif opcion == 2:  
        while True:  
            print("Calcular Área")  
            print("1. Para Círculo")  
            print("2. Para Rectángulo")  
            print("3. Para Cuadrado")  
            print("4. Volver menu principal")  
            opcion3 = int(input("Elija una opción: "))  
            if opcion3 == 1:  
                radio = int(input("Ingrese radio del circulo: "))  
                area = 3.14 * radio * radio  
                print("Área del circulo:", area)  
            elif opcion3 == 2:  
                altura = int(input("Ingrese altura del Rectángulo: "))  
                ancho = int(input("Ingrese ancho del Rectángulo: "))  
                area = altura * ancho  
                print("Área del Rectángulo:", area)   
            elif opcion3 == 3:  
                lado = int(input("Ingrese lado del Cuadrado: "))  
                area = lado * lado  
                print("Área del Cuadrado:", area)  
            elif opcion3 == 4:  
                break              
            else:  
                print("Elección inválida.")  
    elif opcion == 3:  
        break     
    else:  
        print("Elección inválida.")  
 
#Ejercicio 5

ladrillos = int(input("Introduzca el número de ladrillos disponibles: "))
altura = 0
 
utilizados = 0
por_fila = 1
 
while utilizados < ladrillos:
    altura += 1
    por_fila += 1
    utilizados += por_fila
    
print("La altura de la pirámide es de: ", altura)

#Ejercicio 4
import time
 
while True: 
    espacios = ""
    linea = "*"
    for i in range(11):
        print(linea)
        espacios += " "
        linea = espacios + linea
        time.sleep(0.05)
 
    for i in range(14):
        print(linea)
        espacios = " "
        linea = linea[i:] 
        time.sleep(0.05)
    
    linea = "*"
    espacio = " "
    for i in range(22):
        linea +="  *"
        espacio +="   "
    print(linea)
    
    espacio +="*"
    for i in range(14):
        print(espacio)
        time.sleep(0.05)
    print(linea)

