import math


def calculaRaizCuadrada(numero):

    if numero < 0:
        # Forzamos a que salga nuestra propia excepción en caso de que sea negativo
        # Con esto ayudas a que si compartes el código el otro programador sabrá que esto da error
        # y tendra que usar un try except como en la linea 18
        raise ValueError("El número no puede ser negativo")

    else:

        return math.sqrt(numero)


numeroUsuario = (int(input("Introduce número ")))
try:
    print(calculaRaizCuadrada(numeroUsuario))
except ValueError:

    print("Error de número negativo")


print("Y aquí continua el programa")
