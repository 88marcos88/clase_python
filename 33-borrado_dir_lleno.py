import os
import io

# Vamos a borrar un directorio donde hay muchos archivos y desconocemos el nombre
# o a borrar solo un archivo donde si conocemos el nombre pero debemos verificar
# que este dentro del dir

# Generamos el dir y varios archivos en su interior
# borro siempre de inicio xq si existe da error

# os.rmdir("prueba_3")
# os.makedirs("prueba_3")
os.chdir("prueba_3")
print(os.getcwd())

# genero un bucle para crear varios archivos y no hacerlo uno a uno

for i in range(10):
    txt = "Esto es un texto de prueba"
    nombre = "doc" + str(i) + ".txt"
    ax = open(nombre, 'w', encoding='utf8')
    ax.write(txt)
    ax.close()

# Comprobar si el doc esta en el dir y borrado

# pasamos a una lista el nombre de todos los doc y borramos el doc que queremos

lista_doc = os.listdir("./")
doc_a_borrar="doc9.txt"

for i in lista_doc:
    if i == doc_a_borrar:
        os.remove(i)
        print("Archivo encontrado y borrado")
        break # Metemos break para que no siga buscando puesto que ya lo encontró
    print("Archivo no encontrado")

# Para borrarlos todos 

lista_doc = os.listdir("./")
for i in lista_doc:
    os.remove(i)

# Ahora ya podemos borrar el directorio
os.chdir("..")
os.rmdir("prueba_3")

