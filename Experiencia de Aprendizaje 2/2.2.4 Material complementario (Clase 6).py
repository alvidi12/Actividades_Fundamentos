#   ACT 1
#ingreso de liquidación de sueldo
nom = input ("Ingrese nombre empleado: ")
rut = input ("Ingrese rut empleado: ")
horasTrabajadas = int(input ("Ingrese las horas trabajadas: "))
valorHora = int(input("Ingrese el valor hora del empleado: "))
colacion = int(5500)
movilizacion = int(3000)
resultado = (valorHora * horasTrabajadas)+colacion+movilizacion

print(f"-----LIQUIDACIÓN EMPLEADO----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")

#   ACT 2

print("Ingrese los siguientes datos:")
nombre = input("Las 2 primeras letras de su primer nombre: ")
apellido = input("Las 2 primeras letras de su segundo apellido: ")
rut = input("Los 2 primeros números de su rut: ")
mes = input("Las 3 letras iniciales del mes de su nacimiento: ")
ciudad = input("Las 2 últimas letras de la ciudad donde vive: ")
opcion1 = nombre + apellido + rut + mes + ciudad
opcion2 = nombre + rut + apellido + mes + ciudad + mes
opcion3 = rut + nombre + mes + ciudad + apellido
opcion4 = apellido + rut + nombre + mes + ciudad + rut
opcion5 = ciudad + apellido + nombre +rut + mes + ciudad
print("")
print(f"La opción 1 de contraseña es: {opcion1}")
print(f"La opción 2 de contraseña es: {opcion2}")
print(f"La opción 3 de contraseña es: {opcion3}")
print(f"La opción 4 de contraseña es: {opcion4}")
print(f"La opción 5 de contraseña es: {opcion5}")

#   ACT 3

posicionA = "X"
posicionB = ""
posicionC = ""
posicionD = ""
posicionE = "X"
posicionF = ""
posicionG = ""
posicionH = ""
posicionI = "X"
print("")
print("\t\t|\t\t |\t")
print(f"\t{posicionA}\t|\t{posicionB}\t |\t{posicionC}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionD}\t|\t{posicionE}\t |\t{posicionF}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionG}\t|\t{posicionH}\t |\t{posicionI}")
print("\t\t|\t\t |\t")
print("")