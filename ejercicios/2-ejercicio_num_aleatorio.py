import random

aleatorio = random.randint(0, 100)

disparador = 0

print("Adivina el número entre 0 y 100")

while disparador == 0:

    eleccion = int(
        input("Introduce tu respuesta: (si quieres salir introduce -1) "))

    if eleccion == -1:
        print("Adios perdedor")
        break

    if eleccion == aleatorio:
        print("Enhorabuena has acertado")
        disparador += 1
    if eleccion < aleatorio:
        print("El número introducido es menor")
    if eleccion > aleatorio:
        print("El númerop introducido es mayor")
