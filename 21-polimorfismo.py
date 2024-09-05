class Persona():

    def hablar(self):

        return "Hablo como una persona"


class Trabajador(Persona):

    def hablar(self):

        return "Hablo como un trabajador"


class Director(Persona):

    def hablar(self):

        return "Hablo como un director"

# El poli hace que la variable persona en el bucle for cambie de persona a trabajador a director.


def hazlesHablar(listaPersonas):

    for persona in listaPersonas:
        print(persona.hablar())


Antonio = Persona()
Maria = Trabajador()
Ana = Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("----------------------------------")

gente = [Antonio, Maria, Ana]

hazlesHablar(gente)
