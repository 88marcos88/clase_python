def validaUsuario(usu):

    validacion = True

    for i in usu:

        if i.isalnum() == False and i != " ":

            validacion = False

    if len(usu) < 5 or len(usu) > 15:

        validacion = False

    return validacion


a = input("Introduce nombre de usuraio: ")

while validaUsuario(a) == False:

    print("Contraseña no aceptada")
    a = input("Print introduce una contraseña mayor que 5 y meno que 15 que solo contenga número, letras y espacios: ")
