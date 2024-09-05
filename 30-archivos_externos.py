from io import open
# Creamos archivo y escribimos en el
# la opción 'w' es para escribir en el archivo 'r' es leer y 'a' es modificar(append)

archivo_externo = open("primerArchivo.txt", "w", encoding="utf8")

# Añadimos texto mediante write y como parametro se puede pasar el texto o una variable
text = "Usuario"

archivo_externo.write("Bienvenidos a los archivos externos ")
archivo_externo.write(text)
archivo_externo.close()

""" Siempre hay que cerrar un archivo para evitar que siga en ejecución
si queremos evitar tener que esta preocupados por el cierre (en caso de error el archivo
no cerrará se usa 'with' que cierra automaticamente el archio después de trabajar con el
ejemplio: 
"""
# Añadimos mas información método "a"(append) usando el whit para evitar tener que cerrar

with open('primerArchivo.txt', 'a', encoding='utf8') as archivo:
    # \n para hacer salto de linea
    archivo.write("\nAñadimos esta información trasla creación ")

# Para leer archivo linea a linea

archivo2 = open('primerArchivo.txt', 'r', encoding='utf8')

print(archivo2.readline())
print('--------------------------')
print(archivo2.readlines())
print('--------------------------')
print(archivo2.readlines())
print('--------------------------')
# En este caso no va a funcionar el 3 print porque el read tiene un puntero de lectura
# y este se encuentra al final, por eso el print(contenido no devuelve nada)
# Para que leyera deberías de cerrar antes de leer toda la variable o posicionar el puntero
# en la posición 0

contenido = archivo2.read()
print(contenido)
archivo2.close()

# Ejemplo de lectura con with y con variable y read() (lee todo el archivo)
# en vez de readline() que solo lee una linea
# Dependiendo si el archivo es grande, leerlo todo y mostraro por pantalla
# seria muy largo el resultado
with open('primerArchivo.txt', 'r', encoding='utf8') as archivo3:
    contenido = archivo3.read()
    print(contenido)

# Método para almacenart todas las lineas en una lista y poder acceder a la que queramos

with open('primerArchivo.txt', 'r', encoding='utf8') as ax:
    lista = ax.readlines()

    print(lista)

    print(lista[0])

# Manejar el cursor
# Añadimos una 3 linea para poder trabajar con mas lineas
ax = open('primerArchivo.txt', 'a', encoding='utf8')

ax.write("\nAñadimos una tercera linea ")

ax.close()
# Tras la pirmera elctura el cursor estará al final y vamos a desplazarlo al principio
# con el método seek()
with open('primerArchivo.txt', 'r', encoding='utf8') as ax:
    print(ax.read())
    print('--------------------------')
    # El numero es posicion de carácter, no de la linea
    ax.seek(0)
    print(ax.read())
    print('--------------------------')
    # Empezará desde el carácter 6
    ax.seek(6)
    print(ax.read())
    print('--------------------------')
    # Read tmb admite posición de carácter pero este leera hasta ese carácter
    ax.seek(0)
    print(ax.read(6))
    print('--------------------------')
    # Para omitir la primera line usamos el método len, len nos da el tamaño
    # de la linea y posiciona el cursor al final de esta
    ax.seek(0)
    ax.seek(len(ax.readline()))
    print(ax.read())
