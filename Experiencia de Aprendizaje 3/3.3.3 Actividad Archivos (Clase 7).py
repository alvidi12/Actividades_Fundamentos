#Actividad Formativa Archivo
import csv
import json
inferior = []
datoscsv = [
    ['rut','nombre','ventas'],
    [72642413-6,'Comercial Calcetas Runner',150000000],
    [76437473-2,'Reparación Mac',300000000],
    [76254356-9,'ProgramaSoftware',27500000],
    [76077262-3,'Calzados Roma',15000000],
    [76310800-8,'Empresa Arcos',80000000],
    [76283690-4,'Casino Coffe',120000000],
    [76952985-5,'Cafe Express ltda',50000000],
    [76081440-2,'Vino Export SA',20000000],
    [76216579-1,'Cepa Merl LTDA',30000000],
    [76597875-0,'Comercial Ropa America',60000000],
    [76852106-3,'Empresas JP',90000000],
    [76887745-8,'Empresas ICata SA',100000000],
    [76210124-2,'Buses Peñalolen',150000000],
    [76802052-4,'Sandias Paine LTDA',70000000],
    [76575973-1,'Modas Junior P',400000000],
    [76869384-2,'Bar del 81',25000000],
    [76877803-6,'Empresas LLS',8000000],
    [76706124-0,'Empresas luz y vida SA',3000000],
    [76162938-1,'Empresa Matrix',120000000]
]
#aqui segmentamos por cantidad de dinero contribuido y las almacenamos en listas diferentes
pequeño = [registro for registro in datoscsv[1:] if registro[2] <= 100000000]
mediano = [registro for registro in datoscsv[1:] if registro[2] >= 100000001 <= 200000000]
gran = [registro for registro in datoscsv[1:] if registro[2] >= 200000000]
def crear_archivo_csv(nombre_archivo, datos): #creamos un archivo csv que guarde la lista total de los usuarios
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"archivo: {nombre_archivo} creado exitosamente")
crear_archivo_csv('ListadoRutEmpresa.csv', datoscsv)

#creamos una lista con los datos solicitados
datosjson = [
    ['Pequeño Contribuyente'],
    [pequeño],
    ['Mediano Contribuyente'],
    [mediano],
    ['Gran Contribuyente'],
    [gran]
]
def crear_archivo_json(nombre_archivo, datos): #creamos funcion para hacer un archivo json que guarde la lista segmentacion por empresa
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)  
    print(f"archivo JSON: {nombre_archivo} creado exitosamente")
crear_archivo_json('segmentacionEmpresas.json', datosjson)