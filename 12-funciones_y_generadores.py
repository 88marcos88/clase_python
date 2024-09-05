# funcion
def generarPares(limite):

    num = 1

    numerosPares = []

    while num < limite:
        numerosPares.append(num*2)
        num += 1

    return numerosPares


print(generarPares(6))

# generador


def generarParesGenerador(limite):
    # el generador devuelve un objeto iterable por eso hay que volcarlo en una variable
    # y no se imprime como en una función, pero como va generando en base vamos necesitando
    # puede dar valores

    num = 1

    while num < limite:

        yield num*2
        num += 1


sucesionPares = generarParesGenerador(6)

for i in sucesionPares:
    print(i)

# otra forma es con la funcion next de los generadores

sucesionPares2 = generarParesGenerador(6)

print(next(sucesionPares2))

print("Ahora va el siguiete valor: ")

print(next(sucesionPares2))

print(" Quieres otro más? pues ahí lo tienes: ")

print(next(sucesionPares2))
