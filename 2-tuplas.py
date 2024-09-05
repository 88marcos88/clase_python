# Las tuplas son inmutables

misDatosTupla = ("Marcos", 29, 3, 1988)

misDatosLista = ["Marcos", 29, 3, 1988, "Marcos"]

# transforma tupla en lista
misDatosLista2 = list(misDatosTupla)

# transforma lista en tupla
misDatosTupla2 = tuple(misDatosLista)

# comporbar si hay un datos en la tupla
print(29 in misDatosTupla2)

# cuantas veces se encuentra el dato en la tupla
print(misDatosTupla2.count("Marcos"))

# longitud tupla
print(len(misDatosTupla2))

# desempaquetado de tupla(almacena cada valor de la tupla en una variable)
nombre, dia, mes, agno = misDatosTupla

print(misDatosLista2)

print(misDatosTupla2)

print(nombre)
