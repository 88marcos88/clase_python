class Agenda():

    def __init__(self):

        self.miAgenda = {}

    def agregarPersonas(self, nombre, telefono):

        self.miAgenda[nombre] = telefono

    def __len__(self):
        return len(self.miAgenda)


agenda_personal = Agenda()

agenda_personal.agregarPersonas("Marcos", "633686003")
agenda_personal.agregarPersonas("Sandra", "633686003")
agenda_personal.agregarPersonas("mario", "633686003")
agenda_personal.agregarPersonas("yoli", "633686003")
agenda_personal.agregarPersonas("Andrea", "633686003")
agenda_personal.agregarPersonas("Manu", "633686003")

# no funciona porque no da longitud a diccionarios solo a listas/tuplas en este caso si porque hemos creado el metodo __len__
# si borras el método dejaría de funcionar
print(len(agenda_personal))
