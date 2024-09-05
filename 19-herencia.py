class Persona():

    def __init__(self, nombre, apellido, edad):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " edad: " + str(self.edad)

    def habla(self):

        return "Estoy hablando"

    def piensa(self):

        return "Estoy pensando"

    def camina(self):

        return "Estoy caminando"

    def come(self):

        return "Estoy comiendo"


class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):

        super().__init__(nombre, apellido, edad)
        self.escuela = escuela

    def getDatosPersonales(self):

        return super().getDatosPersonales() + " escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"


class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa,):

        super().__init__(nombre, apellido, edad)
        self.empresa = empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " empresa: " + self.empresa

    def trabaja(self):

        return "Estoy Trabajando"


persona1 = Persona("Marcos", "Fluixa", 36)

estudiante1 = Estudiante("Sandra", "Liebana", 31, "UV")

print(estudiante1.getDatosPersonales())

print(persona1.getDatosPersonales())
