from tkinter import *
from tkinter import messagebox
from random import choice

# Definimos un diccionario vacío para almacenar las preguntas y respuestas

preguntas_respuestas = {}

# Función para agregar una pregunta y su respuesta al diccionario

def agregar_pregunta_respuesta(pregunta, respuesta):
    preguntas_respuestas[pregunta] = respuesta

# Función para buscar una respuesta a partir de una pregunta dada

def buscar_respuesta(pregunta):
    if pregunta in preguntas_respuestas:
        return preguntas_respuestas[pregunta]
    else:
        return "Lo siento, no tengo respuesta para esa pregunta."

# Base de datos

agregar_pregunta_respuesta("¿Cuál es la capital de España?", "Madrid")
agregar_pregunta_respuesta("¿Quién escribió Don Quijote de la Mancha?", "Miguel de Cervantes")
agregar_pregunta_respuesta("¿Cuál es el río más largo del mundo?", "El río Nilo")
agregar_pregunta_respuesta("¿Quién escribió la novela 'Don Quijote de la Mancha'?", "Miguel de Cervantes")
agregar_pregunta_respuesta("¿Cuál es el continente más poblado del mundo?", "Asia")
agregar_pregunta_respuesta("¿En qué año terminó la Segunda Guerra Mundial?", "1945")
agregar_pregunta_respuesta("¿Quién fue el primer hombre en pisar la Luna?", "Neil Armstrong")
agregar_pregunta_respuesta("¿Cuál es la capital de Australia?", "Canberra")
agregar_pregunta_respuesta("¿Quién escribió la novela 'Cien años de soledad'?", "Gabriel García Márquez")
agregar_pregunta_respuesta("¿Cuál es el elemento químico más abundante en la corteza terrestre?", "El oxígeno")
agregar_pregunta_respuesta("¿En qué país se encuentra la Torre Eiffel?", "Francia")
agregar_pregunta_respuesta("¿Quién es considerado el padre de la filosofía occidental?", "Sócrates")

# Función que se ejecutará cuando se haga clic en el botón "Botón 1"

def boton1_clic():
    messagebox.showinfo("ON LIVE", "No se puede retornar")

# Función que se ejecutará cuando se haga clic en el botón "Botón 2"

def boton2_clic():
    pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
    respuesta_aleatoria = preguntas_respuestas[pregunta_aleatoria]
    cuadro_texto.config(text=pregunta_aleatoria)
    respuesta.set("Aquí sale la respuesta")
    cuadro_respuesta.delete(0, END)  # Agregar esta línea para borrar el texto del cuadro de respuesta


# Función que se ejecutará cuando se haga clic en el botón "Botón 3"

def boton3_clic():
    pregunta_actual = cuadro_texto.cget("text")
    respuesta_correcta = buscar_respuesta(pregunta_actual)
    respuesta_usuario = cuadro_respuesta.get() 
    if respuesta_usuario.lower() == respuesta_correcta.lower():
        respuesta.set("Tu respuesta es correcta")
    else:
        respuesta.set("La respuesta correcta es: " + respuesta_correcta)

# Crear la ventana principal

ventana = Tk()
ventana.title("ON LIVE")
ventana.geometry("1920x1080")
ventana.config(bg="white")

# Cargar la imagen de fondo

imagen_fondo = PhotoImage(file="img/on_live.png")

# Crear un widget Label para la imagen de fondo

etiqueta_fondo = Label(ventana, image=imagen_fondo)
etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un cuadro de texto en el centro de la ventana superior

cuadro_texto = Label(ventana, width=20, bg="black", fg="medium violet red", font=("gabriola", 50), relief=FLAT)
cuadro_texto.place(x=-5, y=0, width=1920, height=100)

# Barra inferior de respuesta

respuesta = StringVar()
respuesta.set("Aquí sale la respuesta")
cuadro_respuesta = Entry(ventana, width=30, bg="medium violet red", font=("courier", 20), relief=FLAT)
cuadro_respuesta.place(x=680, y=700)
cuadro_texto_respuesta = Label(ventana, textvariable=respuesta, width=60, bg="medium violet red", fg="black", font=("gabriola", 58), relief=FLAT)
cuadro_texto_respuesta.place(x=0, y=890)

# Crear los dos botones de cambio entre preguntas

boton1 = Button(ventana, text="Anterior", command=boton1_clic, bg="black", fg="medium violet red", font=("gabriola", 20), padx=10, pady=5, relief=FLAT)
boton1.pack(side="left", padx=10)

boton2 = Button(ventana, text="Siguiente", command=boton2_clic, bg="medium violet red", fg="black", font=("gabriola", 20), padx=10, pady=5, relief=FLAT)
boton2.pack(side="right", padx=10)

boton3 = Button(ventana, text="Comprobar", command=boton3_clic, bg="gray", fg="blue", font=("gabriola", 20), padx=10, pady=5, relief=FLAT)
boton3.place(x=850, y=480)

# Seleccionar una pregunta aleatoria y mostrarla en el cuadro de texto
pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
cuadro_texto.config(text=pregunta_aleatoria)

# Iniciar el bucle principal de la aplicación

ventana.mainloop()
