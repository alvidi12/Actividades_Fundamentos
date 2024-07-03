#calcular el costo de envío de paquetes para una empresa de logística

print("\n***************************************\nCálculo de costo de envío de paquetes.\nDistancia estandar: 100 Km.\nPeso estandar: 30 kg\nPrecio: $ 5.000\n***************************************\n")

#Ingreso de datos del paquete
while True:
        nombre = input("Ingrese usuario: ")
        if len(nombre) == 0: print("No ha puesto ningun usuario.") 
        elif len(nombre) > 30: print("excedió el límite de caracteres (30)\nVuelva a intentarlo. ")
        else: break


def cantidad_peso():
    while True:
        try:
            peso = float(input("Ingrese peso del paquete (Kg): "))
            return peso
        except ValueError: print("Error de ingreso.")
pesototal = cantidad_peso()

def cantidad_kilometro():
    while True:
        try:
            distancia = float(input("Ingrese distancia de envío (Km): "))
            return distancia
        except ValueError: print("Error de ingreso.")
kilometrototal = cantidad_kilometro()

#Cálculo del costo del envío
costoBase = 5000
exceso_Kg = 500
exceso_Km = 100

if pesototal > 30: PF_kg = (pesototal - 30)*exceso_Kg + costoBase
else: PF_kg = 0

if kilometrototal > 100: PF_km = (kilometrototal - 100)*exceso_Km + costoBase
else: PF_km = 0

CostoTotal = PF_kg + PF_km + costoBase

#Mostrar costo de envío
print(f"Costo de envío:\n\nUsuario: {nombre}\nPeso final paquete: {pesototal} Kg.\nDistancia total: {kilometrototal} Km.\nCosto base de envío: $ {costoBase}\nCosto adicional de peso: ${PF_kg:.0f}\nCosto adicional de Kilometros: ${PF_km:.0f}\nCOSTO TOTAL: ${CostoTotal:.0f}")

#Generar archivo de envío
import os
archivo = "Costos_de_Envio.txt"

with open(archivo, "w")as ruta:
    ruta.write(f"Costo de envio:\n\nUsuario: {nombre}\nPeso final paquete: {pesototal} Kg.\nDistancia total: {kilometrototal} Km.\nCosto base de envio: $ {costoBase}\nCosto adicional de peso: ${PF_kg:.0f}\nCosto adicional de Kilometros: ${PF_km:.0f}\nCOSTO TOTAL: ${CostoTotal:.0f}")

    print("\nSe ha creado un archivo .txt con los datos entregados.")