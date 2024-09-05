def imprime_mensajes():  # función sin parámetros
    print("Esto es un curso de python")
    print("El curso acaba de empezar")
    print("El curso tendrá más de 1500 videos")
    print("Lo anterior es una broma")


def imprime_mensaje2():  # función con parámetros

    return "Este es el mensaje de la función"


def imprime_mensaje_personalizado(mensaje, valor1, valor2):

    # python no suma strings y integer(diferentes tipos de datos)
    return mensaje + str((valor1+valor2))


print(imprime_mensaje_personalizado("la suma es ", 2, 2))

valor_mensaje = imprime_mensaje2()

print(valor_mensaje)

imprime_mensajes()
