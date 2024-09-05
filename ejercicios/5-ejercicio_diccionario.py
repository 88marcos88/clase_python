paises = {}

pais = input("Introduce país: ")

while pais != "salir":

    ciudad = input("Introduce ciudad: ")

    lista_p = paises.setdefault(pais, [ciudad])

    if lista_p != [ciudad]:

        paises[pais].append(ciudad)

    pais = input("Introduce país: ")

print(paises)
