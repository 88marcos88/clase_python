from tkinter import *
from tkinter import messagebox

home = Tk()

home.title("Formulario")
home.config(width=1200, height=900)
main = Frame(home, width=300, height=300)
main.pack()

nombre = Label(main, text="Nombre:")
cuadronombre = Entry(main, fg="red")
cuadronombre.grid(row=0, column=1, padx=15, pady=5)
nombre.grid(row=0, column=0)

apellido = Label(main, text="Apellido:")
cuadroapellido = Entry(main, fg="red")
cuadroapellido.grid(row=1, column=1, padx=15, pady=5)
apellido.grid(row=1, column=0)

telefono = Label(main, text="Teléfono:")
cuadrotel = Entry(main, fg="red")
cuadrotel.grid(row=2, column=1, padx=15, pady=5)
telefono.grid(row=2, column=0)

contra = Label(main, text="Password:")
cuadrocontra = Entry(main, fg="red")
cuadrocontra.config(show="?")
contra.grid(row=3, column=0, padx=15, pady=5)
cuadrocontra.grid(row=3, column=1)

desc = Label(main, text="Descríbete:")
desc.grid(row=4, column=0, padx=15, pady=5)
desctxt = Text(main, width=40, height=10)
desctxt.grid(row=4, column=1, padx=15, pady=5)
scrollVertical = Scrollbar(main, command=desctxt.yview)


def FuncionBoton():

    messagebox.showinfo(
        "hola", "hola " + cuadronombre.get() + " " + cuadroapellido.get())


boton = Button(home, text="Enviar", borderwidth=10, command=FuncionBoton)
boton.pack()

home.mainloop()
