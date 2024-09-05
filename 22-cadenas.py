nUsuario = input("Introduce tu usuario ")

# Imprime la variable en mayúsculas
print("El usuario introducido es: ", nUsuario.upper())
# Imprime la variable en minúsculas
print("El usuario introducido es: ", nUsuario.lower())
# Imprime la variable con la primera en mayúsculas
print("El usuario introducido es: ", nUsuario.capitalize())

edad = input("Introduce tu edad: ")

# is digit devuelve true si edad es un caracter númerico y false si no lo es
while (edad.isdigit() == False):

    print("El valor no es correcto")
    edad = input("Introduce tu edad: ")

if (int(edad) < 18):

    print("No puedes pasar")

else:

    print("Puedes pasar")
