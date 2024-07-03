#Menú de registro de usuarios
usuarios = {}
contrasenas = {}

while True:
    print("\nMenú de opciones:\n1) Iniciar sesión\n2) Registrar usuario\n3) Salir")
    op = input("Seleccione una opción: 1 , 2 , 3 : ")

    if op == "1":  # Iniciar sesión
        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")
        if usuario_ingresado in usuarios and contrasenas[usuario_ingresado] == contrasena_ingresada:
            print("\nInicio de sesión exitoso!!!")
            while True:
                print("\nMenú de inicio sesión:\n1) Realizar llamada\n2) Enviar correo electrónico\n3) Cerrar sesión")
                menu = input("Seleccione una opción: 1 , 2 , 3 : ")

                if menu == "1":
                    celular = input("Ingrese el número de celular (9 dígitos 'Chile'): ")
                    # .isdigit() para una cadena de solo numeros y .startswith() para iniciar con un valor especifico.
                    if celular.isdigit() and len(celular) == 9 and celular.startswith("9"):
                        print(f"\nLlamada realizada al número {celular}.\n")
                    else:
                        print("\nError: El número de celular no es válido.")

                elif menu == "2":
                    correo = input("Ingrese el correo electrónico: ")
                    if "@" in correo:
                        mensaje = input("Ingrese el mensaje a enviar: ")
                        print(f"\nCorreo enviado a {correo}: {mensaje}\n")
                    else:
                        print("Error: El correo electrónico no es válido.")

                elif menu == "3":
                    print("¡Sesión cerrada!")
                    break
                else:
                    print("Error: Opción no válida. Inténtalo nuevamente.")
        else:
            print("Error: Usuario o contraseña incorrectos.")

    elif op == "2": #Crear usuario
        nuevo_usuario = input("Ingrese el nuevo usuario: ")
        nueva_contrasena = input("Ingrese la contraseña para el nuevo usuario: ")
        usuarios[nuevo_usuario] = nueva_contrasena
        contrasenas[nuevo_usuario] = nueva_contrasena
        print(f"Usuario {nuevo_usuario} registrado exitosamente.")

    elif op == "3":
        print("Bye Bye")
        break
    else:
        print("Error: Opción no válida. Inténtalo nuevamente.")