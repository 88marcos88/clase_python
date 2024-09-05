contador = 0

intentos = 1

while contador < 10:
    print("Hola estamos repitiendo el bucle " + str(contador))
    contador = contador+1
print("Acabamos aquí")

edad = int(input("Introduce tu edad "))

while edad < 0 or edad > 150:
    print("Has introducido una edad no valida")
    edad = int(input("Introduce edad valida mierdecilla "))
    contador = contador - 1
    intentos = intentos + 1

    if intentos == 3:
        print("Has introducido erroneamente demasiadas veces")
        break

if contador < 10 and intentos < 3:
    print("la edad del mierdecilla es " + str(edad))
elif contador == 10 and intentos < 3:
    print("Tú edad es " + str(edad))
else:
    print("A dar por el culo a tu casa")
