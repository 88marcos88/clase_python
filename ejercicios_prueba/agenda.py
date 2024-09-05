class Agenda():

    def __init__(self):

        self.agenda = []

    def agregarContacto(self, contacto):

        self.agenda.append(contacto)

    def mostrarContacto(self, n):
        nom = ""
        for i, val in enumerate(self.agenda):
            cn = self.agenda[i].getNombre()
            if cn == n:
                nom = cn
                break
            else:
                nom = "No coincide"

        print(nom)


class Contacto():

    def __init__(self, nombre, telefono):

        self.nombre = nombre
        self.telefono = telefono

    def getNombre(self):

        nombre = self.nombre

        return nombre

    def __str__(self):

        return "El número de teléfono de " + self.nombre + " es " + str(self.telefono)


agendaapple = Agenda()

marcos = Contacto("Marcos", 37)
sandra = Contacto("sandra", 37)
mario = Contacto("mario", 37)
andrea = Contacto("andrea", 37)

agendaapple.agregarContacto(marcos)
agendaapple.agregarContacto(sandra)
agendaapple.agregarContacto(mario)
agendaapple.agregarContacto(andrea)


agendaapple.mostrarContacto("sandra")
