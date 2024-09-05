import datetime


class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # __str__ (equivalente a to string en java) lo que hace es que al imprimir print(p1) (nos daria posicion en memoria y no los datos del objeto)
    # imprime lo que generamos dentro de la función/método
    # cuando pasamos un a variable a string con el método print(str(variable)) es lo mismo que el método __str__
    def __str__(self):

        return "Datos de la persona: /n " + self.nombre + "/n Apellido " + "/n edad: " + str(self.edad)

    # El método __reper_ es similar al __str__ pero más preciso prueba a pasar un dato a reper mediante print(repr(variable))
    # def __repr__(self):

    #   return "Datos de la persona: /n " + self.nombre + "/n Apellido " + "/n edad: " + str(self.edad)
    # ejemplo de diferencia entre ambos métodos

    hoy = datetime.date.today()

    print(str(hoy))
    print(repr(hoy))


p1 = Persona("Marcos", "Gonzalez", 36)

print(p1)

# para generar una funcion que reciba datos indeterminados hay que poner * y eso generará una tupla de datos introducidos
# y si ponemos ** recibe un diccionario


class Persona2():

    alamcen_datos = []

    def __init__(self, *datos):

        for dato in datos:

            self.alamcen_datos.append(dato)

        self.getDatos(datos)

    def getDatos(self, info):

        for dato in info:
            print(dato)


p2 = Persona2("Marcos", "Gonzalez", 36, 56, 56, 34, 346, 7357)


class Persona3():

    def __init__(self, **datos):

        elementos = datos.items()

        for clave, valor in elementos:

            print(clave, " ", valor)


p3 = Persona3(Nombre="Marcos", apellidos="Gonzalez", edad=36)
