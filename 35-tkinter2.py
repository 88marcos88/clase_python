from tkinter import *

raiz = Tk()

raiz.config(bg="violet")
raiz.geometry("800x600")

miFrame = Frame(raiz, width=300, height=300)
miFrame2 = Frame(raiz)
miFrame2.pack(side="right", anchor="n")
miFrame.pack()

# Vamos a crear una etiqueta de texto

label = Label(miFrame, text="chanchito feliz")
# Si lo empaquetamos el div padre (miFrame coge el tamaño de la etiqueta)
# label.pack()
# Pero si queremos que se posicione dentro del padre en vez de empaquetar usamos lo siguiente:
# x= a distancia desde x y= distancia desde y
label.place(x=120, y=125)

# Si no necesitamos editar la etiqueta podemos simplificar de la siguiente forma
# Al crearlo y no asignarle variable luego no puede ser modificado
Label(miFrame, text="Chanchito feliz 2", fg="blue").place(x=120, y=110)
# Vamos a añadir una imagen
# Generamos una variable asignada a una imagen
miImagen = PhotoImage(
    file="/Users/marcosgf/Downloads/Xenoblade_Chronicles_logo2.png")
Label(raiz, image=miImagen).place(x=250, y=320)

# Vamos a generar entry
etiqueta = Label(miFrame2, text="Nombre:")
etiqueta.grid(row=0, column=0, sticky="w")
cuadroTexto = Entry(miFrame2)
etiqueta.config(fg="red")
cuadroTexto.grid(row=0, column=1)

etiqueta2 = Label(miFrame2, text="Apellido:")
etiqueta2.grid(row=1, column=0, sticky="e")
cuadroTexto2 = Entry(miFrame2)
cuadroTexto2.grid(row=1, column=1)


etiqueta3 = Label(miFrame2, text="Telefono:")
etiqueta3.grid(row=2, column=0)
cuadroTexto3 = Entry(miFrame2)
cuadroTexto3.grid(row=2, column=1)

etiqueta4 = Label(miFrame2, text="Direccion de envio de paquetes:")
etiqueta4.grid(row=3, column=0)
cuadroTexto4 = Entry(miFrame2)
cuadroTexto4.grid(row=3, column=1)

raiz.mainloop()
