def divide():

    try:

        op1 = (float(input("Introduce el primer número")))

        op2 = (float(input("Introduce el segundo número")))

        print("El resultado es " + str(op1/op2))

    except ValueError:

        print("Datos erroneos")

    except ZeroDivisionError:

        print("No se puede dividir por 0")

    # Si dejamos vacio el código de error vale para excepciones genericas sea cúal sea el error
    # except:

    #   print("Ha ocurrido un error")

    # El finally hace que el codigo dentro se ejecute aunque haya error o excepción o no.
    # por ejemplo si falla la conexion a la BBDD pones dentro del finally que cierre la conexión para que no consuma recursos
    finally:
        print("Se ha intentado ")


divide()

print("Cálculo finalizado. Continuamos con el programa")
