# Vamos a ver el uso de "continue" "pass" "else(sin estar en condicional if)"
nombre = "marcos gonzalez fluixa"

print(len(nombre))

contador = 0

# pass podemos crear un bucle o una clase aún no definido y dejarlo vacio sin que de error con pass

for i in range(0, 10):
    pass


class EjemploClase:
    pass


# continue saltara el bucle según la condición que le pongamos
for i in nombre:

    if i == " ":  # cada vuelta de bucle si i = a espacio en blanco, salta a la siguiente
        continue
    contador += 1

print(contador)

# else solo se efectuará si el bucle se hace completo(en caso de no encontrar "@")

email = input("Introduce tu email")

for i in email:
    if i == "@":
        arroba = True
        break

else:  # si encuentra "@" nunca entrará en el else
    arroba = False

print(arroba)
