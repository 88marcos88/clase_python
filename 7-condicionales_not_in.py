trabajadores = ["Sandra", "Mario", "Manu", "Yoli", "Andrea"]

if "Manu" in trabajadores:
    print("Manu está en la lista")
else:
    print("Manu no está en la lista")

# tmb se puede buscar en Strings
lenguajes_trim1 = "PHP, Python, c#, HTML"

if "PHP" not in lenguajes_trim1:
    print("falta en la lista")
else:
    print("esta en la lista")

nombre = input("Introduce nombre a buscar ")


def buscar_trabajador(trabajador, empleados):

    if trabajador in empleados:
        print(trabajador + " está en la empresa")
    else:
        print(trabajador + " no está en la empresa")


buscar_trabajador(nombre, trabajadores)
