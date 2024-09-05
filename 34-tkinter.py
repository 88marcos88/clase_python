from tkinter import *

# Primero debemos crear el lienzo con "ventana" con nombre variable=tk()
raiz = Tk()
# Cambiar el titulo
raiz.title("Primera ventana tk")
# Poder denegar o permitir editar el hancho y alto de la ventana 0 = false 1 = true
raiz.resizable(1, 1)
# Dar tamaño por defecto a la ventana
raiz.geometry("800x600")
# Cambiamos el color de la ventana con lo siguiente
raiz.config(bg="blue")

# Ahora vamos a crear los frames (similar a los divs de html5 un contenedor básicamente)
# por defecto vienen vacios (como cuando generas un div en html)
miFrame = Frame()
# Para que el frame forme parte de la raiz ("ventana") debemos empaquetarlos
miFrame.pack()
# Vamos a darle parametros al frame (div) para poder visualizarlo
# Background color
miFrame.config(bg="pink")
# Tamaño
miFrame.config(width="300", height="300")
# Posicionamiento (anchor da la situación "s=sud"
miFrame.pack(side="right", anchor="s")
# Rellena en el eje y la ventana, si pones both rellena la ventana entera
miFrame.pack(fill="y")

# Ejecuta nuestra ventana en loop hasta que la cerremos
raiz.mainloop()
