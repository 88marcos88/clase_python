class Persona():

    # Para encappsular las propiedades se pone un _ para que solo lo puedan usar en herencia y solo en la clase hay que poner dos __
    __nombre = ""
    apellido = ""
    __edad = 0
    genero = "sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre = nombre
        self.apellido = apellido
        self.genero = genero

    def setEdad(self, laedad):

        if laedad < 0 or laedad > 100:
            print("Error en la edad")
        else:
            self.__edad = laedad
            return self.__edad

    def hablar(self):

        return "La persona que se llama " + self.__nombre + " esta hablando"

    def camina(self):

        return "La persona que se llama " + self.__nombre + " esta caminando"

    def getDatos(self):

        return "Nombre: " + self.__nombre + " Apellidos: " + self.apellido + \
            " Edad: " + str(self.__edad) + " Género: " + self.genero


p1 = Persona("Marcos", "Fluixà", "Masculino")

p1.setEdad(36)

print(p1.getDatos())
print(p1.camina())
