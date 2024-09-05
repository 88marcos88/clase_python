from io import open
# Sustituir una linea por otra nueva
# Debemos pasarlo a lista y sustitur una linea por otra pero necesitaremos abrir
# archivo en modo lectura y escritura(append)(r+)

with open('primerArchivo.txt', 'r+', encoding='utf8') as ax:
    list_ax = ax.readlines()
    print(list_ax)
    list_ax[1] = "Es dominguetetetete y ya llega el fin de semana \n"
    # Si no reiniciamos el cursor con seek no escribira donde se encuentre el cursor
    ax.seek(0)
    ax.writelines(list_ax)
    # Para evitar que las lineas se solapen entre documento anterior y la
    # nueva reescritura se usa truncate para que elimine esos posibles fallos
    ax.truncate()


# Bienvenidos a los archivos externos Usuario
# Añadimos esta información tras la creación
# Añadimos una tercera linea
