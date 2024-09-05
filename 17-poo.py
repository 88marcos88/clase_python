class Coche():
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False

    def arrancar(self):
        self.arrancado = True
        print("BRUM BRUM")

    def estadoCoche(self):
        if (self.arrancado == True):
            return "El coche está arrancado"
        else:
            return "El coche no está arrancado"

    # __str__ (equivalente a to string en java) lo que hace es que al imprimir print(p1) (nos daria posicion en memoria y no los datos del objeto)
    # imprime lo que generamos dentro de la función/método
    # cuando pasamos un a variable a string con el método print(str(variable)) es lo mismo que el método __str__
    def __str__(self):

        return "El coche tiene: " + str(self.ruedas) + " ruedas "


miCoche = Coche()
miCoche2 = Coche()

print("Mi coche tiene " + str(miCoche.ruedas) + " ruedas")

miCoche.arrancar()

print(miCoche.estadoCoche())
print(miCoche2.estadoCoche())
