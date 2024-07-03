#1. Test psicologico de 12 preguntas:

print("Bienvenido al test, donde podrás obtener un puntaje de acorde a tu desempeño entregado con estas 12 preguntas:\nResponde con un 'si' o 'no'\n ")
p1 = input("¿Le dedica parte de sus días libre estudiar?\nRespuesta: ")
p2 = input("¿Se considera como un alumno estudioso?\nRespuesta: ")
p3 = input("¿Estudias más de 3 veces a la semana?\nRespuesta: ")
p4 = input("¿Tomas atención en las clases?\nRespuesta: ")
p5 = input("¿Tienes notas de lo realizado en cada clase?\nRespuesta: ")
p6 = input("¿Consideras que aprendes una vez finalizado la clase?\nRespuesta: ")
p7 = input("¿Piensas dedicarle mas tiempo a los estudios una vez finalizado la carrera?\nRespuesta: ")
p8 = input("¿Aplicas lo aprendido durante tu vida diaria?\nRespuesta: ")
p9 = input("¿Te consideras como alguien que quiere seguir aprendiendo?\nRespuesta: ")
p10 = input("¿Corriges tus errores al momento de tenerlos?\nRespuesta: ")
p11 = input("¿Sabes explicarte cuando tienes problemas?\nRespuesta: ")
p12 = input("¿Solucionas solo tus dudas o problemas?\nRespuesta: ")

if p1 == "si":
    p1 = 1
else:
    p1 = 0
if p2 == "si":
    p2 = 1
else:
    p2 = 0
if p3 == "si":
    p3 = 1
else:
    p3 = 0
if p4 == "si":
    p4 = 1
else:
    p4 = 0
if p5 == "si":
    p5 = 1
else:
    p5 = 0
if p6 == "si":
    p6 = 1
else:
    p6 = 0
if p7 == "si":
    p7 = 1
else:
    p7 = 0
if p8 == "si":
    p8 = 1
else:
    p8 = 0
if p9 == "si":
    p9 = 1
else:
    p9 = 0
if p10 == "si":
    p10 = 1
else:
    p10 = 0
if p11 == "si":
    p11 = 1
else:
    p11 = 0
if p12 == "si":
    p12 = 1
else:
    p12 = 0


puntos = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12
if puntos >10: print(f"\nSu puntuación fue de {puntos}. Usted es un alumno con muchos desafíos.")
elif 7 <= puntos <= 9: print(f"\nSu puntuación fue de {puntos} de 15, Usted es un alumno con algunos desafíos.")
elif 4 <= puntos <=6: print(f"\nSu puntuación fue de {puntos} de 15, Usted es un alumno que puede mejorar.")
elif 0 <= puntos <= 3: print(f"\nSu puntuación fue de {puntos} de 15, Usted es un alumno de buen desempeño.")

#2. Validación de información antes del pago:

print("Ingrese los siguientes datos para realizar la compra.\nTodos los datos son obligatorios.\n")
nombre = input("Nombre: ")
telefono = input("Teléfono: ")
producto = input("Ingrese producto y cantidad.\nNombre del producto: ")
cantidad = input("Cantidad: ")
solicitud = input("¿Está seguro que sea pagar?\n('s' o 'n'): ")

if nombre == "cliente"  and telefono == "3344"  and producto ==""  and cantidad == "3" and solicitud == "s":
    print(f"\nFaltan datos por ingresar. Por favor chequee la información ingresada.\nNombre: {nombre}\nTeléfono: {telefono}\nProducto: {producto}\nCantidad: {cantidad}\n\nVuelva a comenzar.")
else: print("Pago realizado")

#3. Creación de videojuego. (Con While)
print("\nJuego: La gran aventura\nPuedes moverte a la derecha 'd', a la izquierda 'a' o hacia adelante 'w'\n\nInicia la aventura")
while True: 
    mov1 = input("Corres hacia la montaña nevada. Un ruido te detiene. (Muevete hacia algun lado): ")
    if mov1 in("a"): break
    else: print("Te aconsejo el otro lado ;)")
print("Ves un gran oso que comienza a avanzar hacia ti")

while True:
    mov2 = input("Te quedas muy quieto. Después de un momento te comienzas a deslizar hacia un lado: ")
    if mov2 in("a"): break
    else: print("Te aconsejo el otro lado ;)")
 
print("Te mueves hacia la izquierda y una planta carnívora te come.\n\nFin de la partida. Muchas gracias por jugar. :D")
