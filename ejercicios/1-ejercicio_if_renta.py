def impositivo_renta(salario):

    porcentaje = ""

    if salario < 12000:
        porcentaje = "7%"

    elif 12000 < salario < 18000:
        porcentaje = "15%"

    elif 18000 <= salario < 35000:
        porcentaje = "21%"

    elif 35000 <= salario < 70000:
        porcentaje = "35%"

    else:
        porcentaje = "45%"

    return "A la renta de " + str(salario) + " le corresponde un " + porcentaje + " de tipo impositivo"


salario2 = int(input("Introduce salario bruto anual "))

print(impositivo_renta(salario2))
