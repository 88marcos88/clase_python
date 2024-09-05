lasCapitales = {"España": "Madrid",
                "Francia": "Paris", "Reino Unido": "Londres"}

lasCapitalesTupla = ("Italia", "Alemania", "Portugal")

# diccionarios anidados

datosJordan = {23: "Jordan", "Nombre": "Michael", "Equipo": "C.Bulls",
               "Anillos": {"temporadas": [1991, 1992, 1996, 1997]}}

print(datosJordan)
print('------------')
print(datosJordan.keys())
print('------------')
print(datosJordan["Anillos"])
print('------------')

# crear diccionario desde una tupla
otrasCapitales = {lasCapitalesTupla[0]: "Roma",
                  lasCapitalesTupla[1]: "Berlin", lasCapitalesTupla[2]: "Lisboa"}

print(otrasCapitales)

datos = {"tipo": "guerrero", "ataque": 100, "defensa": 60, "inteligencia": 30}

# aumentamos el ataque
datos["ataque"] += 20

print(datos)

# añadir valores/modificar
lasCapitales["Colombia"] = "Bogota"

# borrar valor
del lasCapitales["Reino Unido"]

# ver dato de un valor
print(lasCapitales["España"])

# ver las claves del dicionario
print(lasCapitales.keys())

# ver datos del dicionario
print(lasCapitales.values())

# longitud dicionario
print(len(lasCapitales))

print(lasCapitales)

# borra o limpiar el diccionario

datosJordan.clear()  # limpia
del lasCapitales  # borrada, si borramos no existe no se puede imprimir dará error

print("limpias" + str(datosJordan))

print(datos.items())

# bucle que multiplica por dos los valores
datos2 = {k: v*2 for (k, v) in datos.items()}
print(datos2)
