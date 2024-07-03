"""
1. Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla utilizando doble for, mostrar los elementos por pantalla de forma ordenada como una matriz, tal cual muestra el ejemplo:

	 3	10	 4	16
	 1	 7 	 8	-7
	 9	-1	 3	 9
"""

matriz_2d_arreglo =[
    [3,10,4,16],
    [1,7,8,-7],
    [9,-1,3,9]
]
for i in matriz_2d_arreglo:
    for l in i:
        print(i)

"""
2. Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
Una vez completado, mostrar la siguiente información:
●	Número de elementos “amarillo”.
●	Número de elementos “rojo”.
●	Número de elementos “Naranja”.
●	Número de elementos “Verde”.
●	Número de elementos “Blanco”
"""
matriz_3d_conteo = [
    [["amarillo"], ["Verde"], ["Naranja"]],
    [["Blanco"], ["Naranja", "amarillo"], ["Blanco"]],
    [["Verde"], ["Naranja"], ["rojo"]]
]

colores = {"amarillo": 0, "rojo": 0, "Naranja": 0, "Verde": 0, "Blanco": 0}
for capa in matriz_3d_conteo:
    for fila in capa:
        for elemento in fila:
            colores[elemento] += 1

for color, cantidad in colores.items():
    print(f"Número de elementos '{color}': {cantidad}")

"""
3. Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma automática los números de asiento y luego mostrarlo por pantalla 
de la siguiente forma
1	2		3	4
5	6		7	8
9	10		11	12
13	14		15	16
17	18		19	20
21	22		23	24
25	26		27	28
29	30		31	32
33	34		35	36
37	38		39	40
"""

filas = 10
columnas = 4
bus = [[0] * columnas for _ in range(filas)]

# Asignar números de asiento automáticamente
numero_asiento = 1
for fila in range(filas):
    for columna in range(columnas):
        bus[fila][columna] = numero_asiento
        numero_asiento += 1

for fila in bus:
    print(*fila, sep="\t")