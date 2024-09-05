# set sirve para generar una lista poco pesada sin marcadores de posicion y sin elementos
# repetidos

sistema_solar = "Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno Plutón tierra"

# Generamos un set y estara vacio y no repite elementos del string como el caso de tierra
planetas = set()

# Lo llenamos con un bucle for, split es para indicar que separa las palabras sino separa
# por letra
for planeta in sistema_solar.split(" "):
    planetas.add(planeta)

print(planetas)

# Si queremos generar un set con todo el conjunto y sin repeticiones para localizar
# una letra, lo haremos de la siguiente forma.
# Al no hacerse con un bucle no se le puede pasar el separador y todo el string es
# uno completo y sin repeticiones
print("------------")
planetas2 = set(sistema_solar)
print(planetas2)
