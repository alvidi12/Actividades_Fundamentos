#EJERCICIO 1 Calculadora con funciones e incorporación de sentencias de validación
print("Calculadora\n1. Suma\n2. Resta\n3. Multiplica\n4. Divide\n5. Salir")
op = int(input("Escoge el numero de la operacion deseada: "))
def validar_numero(entrada):
    try:
        return float(entrada)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return None

if op == 1:
    def sumar(num1, num2):
        suma = num1 + num2
        print(f"La suma es: {suma}")

    num1 = input("Primer número: ")
    num1 =validar_numero(num1)
    num2 = input("Segundo número: ")
    num2 =validar_numero(num2)
    sumar(num1, num2)

elif op == 2:
    def resta(num1, num2):
        resta = num1 - num2
        print(f"La resta es: {resta}")

    num1 = input("Primer número: ")
    num1 =validar_numero(num1)
    num2 = input("Segundo número: ")
    num2 =validar_numero(num2)
    resta(num1, num2)

elif op == 3:
    def multi(num1, num2):
        multi = num1 * num2
        print(f"La multiplicacion es: {multi}")

    num1 = input("Primer número: ")
    num1 =validar_numero(num1)
    num2 = input("Segundo número: ")
    num2 =validar_numero(num2)
    multi(num1, num2)

elif op == 4:
    def div(num1, num2):
        div = num1 / num2
        print(f"La division es: {div}")

    num1 = input("Primer número: ")
    num1 =validar_numero(num1)
    num2 = input("Segundo número: ")
    num2 =validar_numero(num2)
    div(num1, num2)

else:
    print("Saliste de calculadora")