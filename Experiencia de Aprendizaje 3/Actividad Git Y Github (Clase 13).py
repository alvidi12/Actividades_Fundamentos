import statistics as st

datos_numeros = ("10\n20\n20\n30\n40\n50\n50\n60\n")
with open('datos.txt', 'w') as archivo:
    archivo.writelines(datos_numeros)
print(f"Datos de 'datos.txt'\n{datos_numeros}")

try:
    with open('datos.txt', 'r') as datos:
        numeros = datos.read().splitlines()
        intConvertor = [int (i) for i in numeros]   #Convertidor de string a integer
        numeros = intConvertor
        mediana = st.median(numeros)
        promedio = sum(numeros) / len(numeros)
        promFinal = round(promedio,1)
        moda = st.mode(numeros)

    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")

except:
    print("ERROR: ERROR EN EL PROGRAMA. CONSULTAR AL DUEÑO")