fruteria = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

en = input("Introduce fruta: ")

if en.title() not in fruteria:
    print("Fruta no disponible.")

else:
    kg = int(input('Introduce kg: '))
    print('El precio total a pagar es: ' + str(fruteria[en.title()]*kg) + '€')
