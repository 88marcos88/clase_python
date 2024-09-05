import os
import io

# Crear directorio donde estamos trabajando
# Comento la linea de creación porque una vez creado si se ejecuta otra vez da error
# porque ya existe

# os.makedirs("prueba_directorio")

# pwd

print(os.getcwd())

# Moverse de direcctorio y creamos ahí un archivo txt llamado prueba.txt

os.chdir("prueba_directorio2")

print(os.getcwd())

ax = open("prueba.docx", "w", encoding="utf8")

ax.write("Esto es un texto de prueba")

# Mostrar lo que hay en el directorio desde su raiz (en lista)
print(os.listdir("./"))

# Renobrar archivo, primer parametro nombre de archivo original y segundo nombre nuevo

os.rename('prueba.docx', 'archivo_a_eliminar.docx')

# Eliminar archivo

os.remove('archivo_a_eliminar.docx')

# Eliminar directorio chdir("..") para volver a su directorio padre y
# poder borrarlo (sino no encontrará el directorio) y
# (no dejará si tiene archivos en su interior)

os.chdir("..")
# comento el borrado de dir xq si salta el error ya no sigue el programa
# os.rmdir('prueba_directorio2')

# Eliminamos el archivo y luego borramos el directorio

os.chdir("prueba_directorio2")
os.remove('prueba.txt')
os.chdir("..")
os.rmdir('prueba_directorio2')
