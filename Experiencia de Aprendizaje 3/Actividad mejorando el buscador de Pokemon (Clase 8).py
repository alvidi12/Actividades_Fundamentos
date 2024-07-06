import tkinter as tk #importa el modulo tkinter para la interfaz grafica
import requests #importa un modulo para hacer las solicitudes http a la API
import random

from io import BytesIO #importa IO para los datos binarios
from PIL import Image, ImageTk #para trabajar con las imagenes de los poke

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url) #solicitud get a la API mediante la URL

    if response.status_code == 200: #200 verifica si la solicitud fue exitosa
        data = response.json() #convierte la respuesta en un formato json()
        nombre = data["name"] #obtenemos el nombre del poke
        numero = data["id"] #numero del poke
        tipos = [tipos["type"]["name"] for tipos in data ["types"]] #obteniendo el tipo de poke
        ataque = [ataque["stat"]["name"] for ataque in data ["stats"]]
        
        resultado = f"Nombre: {nombre}\n Número: {numero}\n Tipos: {', '.join(tipos)}\n Ataque: {ataque}" #creamos cadena con saltos de linea para obtener los datos del poke 

        imagen_url = data["sprites"]["front_default"] #obteniendo la imagen url con los datos de la API

        response_imagen = requests.get(imagen_url) #realiza una solicitud get a la url
        imagen = Image.open(BytesIO(response_imagen.content)) #abre la imagen con BytesIO
        imagen = imagen.resize((500,500), Image.Resampling.LANCZOS) #redimensiona la imagen
        foto = ImageTk.PhotoImage(imagen) #convierte la imagen en un objeto 
        label_imagen.config(image=foto)
        label_imagen.image = foto #guarda la referencia de la imagen
    else:
        resultado = "No se encontró el pokemón, escribe bien pues o atrapalo minimo"
        label_imagen.config(image=None) #elimina la imagen si no encuentra el pokemon

    label_resultado.config(text=resultado) #configura la etiqueta label para mostrar la info del poke


def buscar_poke_aleatorio():
    random_poke = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{random_poke}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombre = data["name"]
        numero = data["id"]
        tipos = [tipos["type"]["name"] for tipos in data ["types"]]

        resultado = f"Nombre: {nombre}\n Número: {numero}\n Tipos: {', '.join(tipos)}"

        imagen_url = data ["sprites"]["front_default"]

        response_imagen = requests.get(imagen_url)
        imagen = Image.open(BytesIO(response_imagen.content))
        imagen = imagen.resize((500,500), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)
        label_imagen.config(image=foto)
        label_imagen.image = foto
    else:
        resultado = "No se encontro Pokemon"
        label_imagen.config(image=None)

    label_resultado.config(text=resultado) 

window = tk.Tk() #creamos ventana principal de la aplicacion
window.title("Busca tu pokemon")

label_pokemon = tk.Label(window, text="Ingresa el nombre del pokemon")
label_pokemon.pack()

entry_pokemon = tk.Entry(window) #Crea una entrada de datos, para recibir el nombre del pokemon
entry_pokemon.pack() #empaqueta el campo, muestra en ventana

button_buscar = tk.Button(window, text="Buscar", command=buscar_pokemon)
button_buscar.pack() #Empaqueta el boton en la ventana

button_random = tk.Button(window, text="Buscar Aleatorio", command=buscar_poke_aleatorio)
button_random.pack()

label_resultado = tk.Label(window, text="") #Creamos una  etiqueta vacia para mostrar los resultados de la busqueda
label_resultado.pack()

label_imagen = tk.Label(window) #Etiqueta para mostrar el poke
label_imagen.pack()

window.mainloop() #inicia el bucle principal para que se ejecute la aplicacion