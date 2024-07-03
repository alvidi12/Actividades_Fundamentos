#1) Frecuencia de Palabras en un Texto
nombre1 =input("Nombre 1:")
nombre2 =input("Nombre 2:")
nombre3 =input("Nombre 3:")
lista = [nombre1, nombre2, nombre3]

if len(nombre1) > len(nombre2):
    lista = [nombre1]
if len(nombre2) > len(nombre3):
    lista = [nombre2]
if len(nombre3) > len(nombre1):
    lista = [nombre3]
print(f"El nombre con mayor caractéres es: {lista}")

#2) Creacion de lista de 3 nombres y 3 apellidos
nombre1 =input("Nombre 1:")
apellido1=input("Apellido 1:")
nombre2 =input("Nombre 2:")
apellido2=input("Apellido 2:")
nombre3 =input("Nombre 3:")
apellido3=input("Apellido 3:")

lista1 = [nombre1, nombre2, nombre3]
lista2 = [apellido1, apellido2, apellido3]

print("\nNombres:")
for lista1 in lista1:
    print(f"- {lista1}")
print("\nApellidos:")
for lista2 in lista2:
    print(f"- {lista2}")

#3) Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower() y upper() ) . Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.
lista_nombres = []
while True:
    nombre = input("Ingrese un nombre (o 'no' para terminar): ")
    if nombre.lower() == "no":
        break
    lista_nombres.append(nombre)

if lista_nombres:
    nombre_mas_corto = min(lista_nombres, key=len)
    lista_nombres.remove(nombre_mas_corto)
    print(f"Nombre más corto eliminado es: {nombre_mas_corto}")
else:
    print("No se ingresaron nombres.")

#4) Crear diccionario para almacenar usuarios y contraseñas
usuarios = {}
while True:
    print("\nMenú:\n1. Iniciar sesión\n2. Registrar usuario\n3. Eliminar usuario\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("sesión valida.\n")
        else:
            print("Error: Usuario o contraseña incorrectos.\n")

    elif opcion == "2":
        nuevo_usuario = input("Ingrese un nuevo usuario: ")
        nueva_contrasena = input("Ingrese una contraseña: ")
        usuarios[nuevo_usuario] = nueva_contrasena
        print(f"Usuario {nuevo_usuario} registrado correctamente.\n")

    elif opcion == "3":
        usuario_eliminar = input("Ingrese el nombre de usuario a eliminar: ")
        if usuario_eliminar in usuarios:
            contrasena_confirmar = input("Ingrese su contraseña para confirmar: ")
            if usuarios[usuario_eliminar] == contrasena_confirmar:
                del usuarios[usuario_eliminar]
                print(f"Usuario {usuario_eliminar} eliminado correctamente.")
            else:
                print("Error: Contraseña incorrecta.")
        else:
            print("Error: Usuario no encontrado.")

    elif opcion == "4":
        print("Bye Bye")
        break
    else:
        print("Error. Inténtelo nuevamente.\n")

#5) Lista de supermercado
productos = {}
while True:
    print("\nMenú de supermercado:\n1. Agregar productos\n2. Ver canasta\n3. Ver total\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        productos[nombre_producto] = precio_producto
        print(f"{nombre_producto} agregado al catálogo.\n")

    elif opcion == "2":
        print("Productos del catálogo:")
        for producto, precio in productos.items():
            print(f"{producto}: ${precio:.2f}")

    elif opcion == "3":
        carrito = []
        while True:
            producto_seleccionado = input("Ingrese un producto, o ecriba 'no' para terminar: ")
            if producto_seleccionado.lower() == "no":
                break
            if producto_seleccionado in productos:
                carrito.append(producto_seleccionado)
                print(f"{producto_seleccionado} agregado al carrito.\n")
            else:
                print("Producto no válido.")
        total = sum(productos.get(producto, 0) for producto in carrito)
        print(f"Total a pagar: ${total:.2f}\n")

    elif opcion == "4":
        print("¡Gracias por su compra!")
        break
    else:
        print("Opción no válida. Inténtelo nuevamente.")
