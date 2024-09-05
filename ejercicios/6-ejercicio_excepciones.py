lista_nombres = []

while len(lista_nombres) < 10:

    nombre = input("Introduce un nombre: ")

    if nombre in lista_nombres:

        raise nombreDuplicado("El nombre esta en la lista, prueba con otro")

    else:

        lista_nombres.append(nombre)
