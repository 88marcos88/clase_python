from tkinter import *

raiz = Tk()

calc = Frame(raiz)
display = Frame(raiz)
display.pack()
calc.pack()

intro = StringVar(value="0")


def FuncionBoton(num):
    if intro.get() == '0':
        intro.set(num)
    else:
        intro.set(intro.get() + num)


resultado = Entry(display, textvariable=intro)
resultado.grid(row=0, column=0)

num1 = Button(calc, text="1", command=lambda: FuncionBoton("1"))
num1.grid(row=3, column=0)
num2 = Button(calc, text="2", command=lambda: FuncionBoton("2"))
num2.grid(row=3, column=1)
num3 = Button(calc, text="3", command=lambda: FuncionBoton("3"))
num3.grid(row=3, column=2)
nummenos = Button(calc, text="-")
nummenos.grid(row=3, column=3)

num4 = Button(calc, text="4", command=lambda: FuncionBoton("4"))
num4.grid(row=2, column=0)
num5 = Button(calc, text="5", command=lambda: FuncionBoton("5"))
num5.grid(row=2, column=1)
num6 = Button(calc, text="6", command=lambda: FuncionBoton("6"))
num6.grid(row=2, column=2)
numdiv = Button(calc, text="/")
numdiv.grid(row=2, column=3)

num7 = Button(calc, text="7", command=lambda: FuncionBoton("7"))
num7.grid(row=1, column=0)
num8 = Button(calc, text="8", command=lambda: FuncionBoton("8"))
num8.grid(row=1, column=1)
num9 = Button(calc, text="9", command=lambda: FuncionBoton("9"))
num9.grid(row=1, column=2)
numx = Button(calc, text="x")
numx.grid(row=1, column=3)

num0 = Button(calc, text="0", command=lambda: FuncionBoton("0"))
num0.grid(row=4, column=0)
numpunto = Button(calc, text=".", command=lambda: FuncionBoton("."))
numpunto.grid(row=4, column=1)
numigual = Button(calc, text="=")
numigual.grid(row=4, column=2)
nummas = Button(calc, text="+")
nummas.grid(row=4, column=3)

raiz.mainloop()
