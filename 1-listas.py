trabajadores = ["Sandra", "Mario", "Yoli", "Manu", 10]

trabajadoresB = ["Manolo", "Juan", "Susana", "Maria", "Sandra"]

print(len(trabajadores))

print(trabajadores[0])

print(trabajadores[-1])

print(trabajadores[0:3])


# añadir un valor
trabajadores.append("Andrea")

# modificar valor
trabajadores[3] = "Marcos"
print(trabajadores)

# eliminar valor
# tmb con trabajadores.remove("Maria") no funciona con indices para borrar con indice trabajadores.pop(0)
del trabajadores[4]
print(trabajadores)

# añadir varios valores
# o con el metodo extend trabajadores.extend(["Rafa", "Paqui"])
trabajadores += ["Rafa", "Paqui"]
print(trabajadores)

# invertir la lista solo la imprime no modifica la lista original
print(list(reversed(trabajadores)))

# para modificarla "OJO va sin D al final, no como la anteriro funcion"
trabajadores.reverse()

print(trabajadores)

# repetir la lista X veces
print(trabajadores*2)

# concadenar listas sin modificar original
print(trabajadores + trabajadoresB)

# concadenar modificando la original,
# con extend la añadimos a la original con append se añadira como sublista
trabajadores.extend(trabajadoresB)
print(trabajadores)

trabajadoresB.append(trabajadores)
print(trabajadoresB)

# borrar una lista
trabajadoresB.clear()

print(trabajadoresB)

# saber cuantas veces aparece un elemento

print(trabajadores.count("Sandra"))

# buscar el indice de un elemento (si el elemento esta mas de una vez solo aparece el primer indice)
# si no existe dara un error
print(trabajadores.index("Sandra"))

# ordenar una lista con método short() Si la lista está previamente ordenada, entonces la consola retornará "None".

mi_lista = [67, 2, 999, 1, 15]

mi_lista.sort()

# si queremos que sea invertida mis_lista.sort(reverse=True)

print("Lista Ordenada: ", mi_lista)

# para que se imprima todo en la misma linea agrega end=" "

ganadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ganadores.sort(reverse=True)

for i in ganadores:

    print(i, end=",")

trabajadores.pop(0)

print(trabajadores)
