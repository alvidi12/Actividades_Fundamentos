def validar_lista_numeros():
    while True:
        solicitud = input("Ingrese una lista de números enteros separados por espacios: ")
        try:
            solicitud = [int(numero) for numero in solicitud.split()]
            return solicitud
        except ValueError:
            print("Error")
valido = validar_lista_numeros()

numeros_pares = []
numeros_impares = []
for numero in valido:
    if numero % 2 == 0:
        numeros_pares.append(numero)
        print(f"Los números pares son: {numeros_pares}")
    else:
        numeros_impares.append(numero)
        print(f"Los números impares son: {numeros_impares}")