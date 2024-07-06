#EJERCICIO 1 Validación de usuarios
import csv
import json
mayores = []

#Creamos la lista que contiene los datos
datos_csv = [
    ['Nombre', 'Edad', 'Comuna'],
    ['Juan', 21, 'Puente Alto'],
    ['Maria', 30, 'Concepcion'],
    ['Carlos', 22, 'Viña del Mar'],
    ['Estela', 25, 'Puerto Montt']
]

mayores = [registro for registro in datos_csv[1:] if registro[1] >= 25] #Realiza el registro dentro de la lista para verificar cual es mayor a 25 años y los agrega a la lista creada

def crear_archivo_csv(nombre_archivo, datos): #creamos un archivo csv que guarde la lista total de los usuarios
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)   
    print(f"archivo: {nombre_archivo} creado exitosamente")
crear_archivo_csv('Lista_usuarios.csv', datos_csv)
def crear_archivo_json(nombre_archivo, datos): #creamos funcion para hacer un archivo json que guarde la lista mayores
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)   
    print(f"archivo JSON: {nombre_archivo} creado exitosamente")
crear_archivo_json('Lista_mayores_edad.json', mayores)

#EJERCICIO 2 ganadores de sorteo
info_csv = [
    ['Rut','Digito verificador','Nombre'],
    [10744679,-6,'Jose Haro'],
    [19881120,-3,'Daniela Almonacid'],
    [16112356,-0,'Carlos González'],
    [17651562,-7,'Andrea Soto'],
    [13429495,-7,'Luis Torres'],
    [17470063,'-K','Maria Rodríguez'],
    [19089980,-2,'Pablo Fernández'],
    [17449807,-5,'Valentina Pérez'],
    [13154134,-1,'Nicolás Vargas'],
    [14073175,-7,'Antonella Muñoz'],
    [24052019,-2,'Felipe Silva'],
    [27779771,-2,'Sofía López'],
    [23135155,-8,'Juan Díaz'],
    [25449950,-1,'Isabel Castro'],
    [22398351,-0,'Diego Morales'],
    [20449542,-4,'Ana Smith'],
    [27730053,-2,'Matías Araya'],
    [27358198,-7,'Valeria Mendoza'],
    [25130662,-1,'Gabriel Pérez'],
    [24981167,'-K','Martina Ruiz'],
    [22096175,-3,'Sebastián Herrera'],
    [23010574,'-K','Francisca Flores'],
    [24218263,-4,'Ricardo González'],
    [28942147,-5,'Constanza Álvarez'],
    [27165749,-8,'Javiera Troncoso'],
    [22216307,-2,'Eduardo Navarro'],
    [22425010,'-K','Catalina Vargas'],
    [23811768,-2,'Ángela Soto'],
    [24661213,-7,'Cristian Mora'],
    [20781422,-9,'Carla Contreras'],
    [10363927,-1,'Mauricio Rojas'],
    [12598545,-9,'Marcela Fernández'],
    [19105327,-3,'Felipe Montes'],
    [19539754,-6,'Alejandra Oyarzún'],
    [15731749,-0,'Pedro Ramírez'],
    [12865638,-3,'Daniela Aravena'],
    [10294021,-0,'Francisco Valdés'],
    [14104975,-5,'Florencia Rojas'],
    [11975810,-6,'Rodrigo Gómez'],
    [17500269,-3,'Amanda Guzmán']
]
numeros_texto = [str(registro[0]) for registro in info_csv[1:]]
ganadores = [elemento for elemento in numeros_texto if elemento[-2:] in ('92', '95', '84')] #solo funciona con un ganador siendo que hay 2
print(ganadores)
def crear_archivo_csv(nombre_archivo, datos): #creamos un archivo csv que guarde la lista total de los usuarios
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"archivo: {nombre_archivo} creado exitosamente")
crear_archivo_csv('ListadoRun.csv', info_csv)
def crear_archivo_json(nombre_archivo, datos): #creamos funcion para hacer un archivo json que guarde la lista mayores
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)  
    print(f"archivo JSON: {nombre_archivo} creado exitosamente")
crear_archivo_json('ganadores.json', ganadores)