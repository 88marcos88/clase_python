lista1 = ["sandra", "Marcos", 10, 11]
lista2 = ["sandra", "Marcos", 10, 11]
lista3 = ["sandra", "Marcos", 10, 12]

iguales = True

if len(lista1) != len(lista3):

    iguales = False
else:
    for i in range(0, len(lista1)):

        if (lista1[i] != lista2[i]):
            iguales = False

print(iguales)

for x in range(0, 3):
    print(lista1[x])
