def suma(num1, num2):
    return num1+num2


def resta(num1, num2):
    return num1-num2

# si dividimos entre 0 la división dará infinito (error)
# def multiplica(num1, num2):
#    return num1*num2


def multiplica(num1, num2):
    return num1*num2


def divide(num1, num2):

    # "Controlamos" el error con try "Intenta"
    try:
        return num1/num2
    # Marcamos el codigo de error que puede producirse y que hacer en caso de que ese error salte
    except ZeroDivisionError:
        print("no se puede dividir entre zero")
        return "operación erronea"


contador = 0
while True:
    try:

        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))

        break

    except ValueError:
        if contador < 3:
            print("Los valores no son correctos, solo números")
            contador += 1
        else:
            break
if contador < 3:
    operacion = input(
        "Introduce la operación a realizar (suma,resta,multiplica,divide): ")

    if operacion == "suma":
        print(suma(op1, op2))

    elif operacion == "resta":
        print(resta(op1, op2))

    elif operacion == "multiplica":
        print(multiplica(op1, op2))

    elif operacion == "divide":
        print(divide(op1, op2))

    else:
        print("Operación no contemplada")
else:
    print("has introducido valores incorrectos muchas veces")


print("Operación ejecutada. Continuación de ejecución del programa ")
