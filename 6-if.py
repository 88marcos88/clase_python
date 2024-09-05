def evaluar_alumno(nota):
    valoracion = "desconocida"
    if nota < 5:
        valoracion = "suspendido"
    elif nota >= 5 and nota < 6:
        valoracion = "suficiente"
    elif nota >= 6 and nota < 7:
        valoracion = "bien"
    elif nota >= 7 and nota < 8:
        valoracion = "notable"
    elif nota >= 8 and nota < 9:
        valoracion = "excelente"
    elif nota > 9:
        valoracion = "excelsior"
    else:
        valoracion = "cagaste"

    return valoracion


nota_alumno = int(input("Introduce la nota: "))
print(evaluar_alumno(nota_alumno))
