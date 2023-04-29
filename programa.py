from tkinter import *
from tkinter import messagebox

# Función que se ejecutará cuando se haga clic en el botón "Botón 1"
def boton1_clic():
    texto.set("¡Has pulsado el botón 1!")

# Función que se ejecutará cuando se haga clic en el botón "Botón 2"
def boton2_clic():
    texto.set("¡Has pulsado el botón 2!")

# Función que se ejecutará cuando se haga clic en el botón "Botón 3"
def boton3_clic():
    respuesta_usuario = cuadro_respuesta.get() # Obtener la respuesta del usuario desde la caja de entrada
    respuesta_correcta = "respuesta_correcta" # Aquí deberías cambiarlo por la respuesta correcta de tu pregunta
    if respuesta_usuario.lower() == respuesta_correcta.lower():
        messagebox.showinfo("ON LIVE", "Tu respuesta es correcta")
    else:
        messagebox.showinfo("ON LIVE", "No es correcta esa respuesta")

# Crear la ventana principal

ventana = Tk()
ventana.title("ON LIVE")
ventana.geometry("800x450")
ventana.config(bg="gray")

# Crear un objeto StringVar para almacenar el texto del cuadro de texto

pregunta = StringVar()

# Configurar el valor inicial del cuadro de texto

pregunta.set("Aquí sale la pregunta")
frame_operaciones = Frame(ventana)
frame_operaciones.config(bg="black", width=780, height=150)
frame_operaciones.place(x=10,y=10)

# Barra inferior de respuesta

respuesta = StringVar()

# Configurar el valor inicial del cuadro de texto

respuesta.set("Aquí sale la respuesta")
frame_operaciones_2 = Frame(ventana)
frame_operaciones_2.config(bg="white", width=780, height=150)
frame_operaciones_2.place(x=10,y=290)

# Añadir respuesta de usuario

cuadro_respuesta = Entry(frame_operaciones_2, width=30)
cuadro_respuesta.place(x=250, y=50)
cuadro_respuesta.config(bg="white", font="courier")

# Crear un cuadro de texto en el centro de la ventana superior

cuadro_texto = Label(ventana, textvariable=pregunta, width=20)
cuadro_texto.place(x=300, y=10)
cuadro_texto.config(bg="black", fg="red", font=("gabriola", 20))

# Crear un cuadro de texto en el centro de la ventana inferior

cuadro_texto = Label(ventana, textvariable=respuesta, width=20)
cuadro_texto.config(bg="white", fg="green", font=("gabriola", 20))
cuadro_texto.place(x=300, y=380)

# Crear los dos botones de cambio entre preguntas

boton1 = Button(ventana, text="Anterior", command=boton1_clic)
boton1.pack(side="left", padx=10)
boton1.config(bg="black", fg="red", font=(", 10"))

boton2 = Button(ventana, text="Siguiente", command=boton2_clic)
boton2.pack(side="right", padx=10)
boton2.config(bg="white", fg="green", font=(", 10"))

# Crear el botón de comprobar

boton3 = Button(ventana, text="Comprobar", command=boton3_clic)
boton3.place(x=370, y=215)
boton3.config(bg="gray", fg="blue", font=(", 10"))

# Iniciar el bucle principal de la aplicación

ventana.mainloop()
