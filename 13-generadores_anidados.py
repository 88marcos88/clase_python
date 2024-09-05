def capitalesDelMundo(*ciudades):
    # el asterico quiere decir que vamos a pasarle parametros indefinidos en una funcion normal,
    # si quieres pasarle dos seria capitalesDelMundo(ciudad1,ciudad2), el asterisco lo guardará
    # en una tupla
    for capital in ciudades:
        # for letra in capital:
        yield from capital  # El yield from sustituye al for para bucles anidados


capitales_devueltas = capitalesDelMundo("Valencia", "Madrid", "Barcelona")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
