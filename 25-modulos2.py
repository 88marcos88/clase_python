
# Todo lo que vemos acontinuación solo funciona si estan ambos archivos en la misma carpeta, para que funcionen
# desde distintas carpetas hay que usar paquetes para convertir una carpeta en paquete solo hay que crear un archivo
# __init__.py y luego referencia a esa carpeta en el import.
# Al importar el módulo, para hacer uso de sus funciones, hay que llamar a la funcion con el nombre del módulo
# ejemplo: modulos1.sumar(1, 2).
import modulos.modulos1 as modulos1

# Para evitar tener que llamar al módulo entero, se puede importar la clase o las clases del módulo mediante from y de esta forma
# no se tiene que llaamr al módulo + función.

from modulos.modulos1 import restar, multiplicar

restar(5, 2)

multiplicar(5, 5)

modulos1.sumar(1, 2)

# Para no importar una a una si las necesitamos todas hay que poner * from modulos1 import * (si no se usan todas las funciónes)
# no es recomendable porque consumirá más memoria que solo importar las que vas a usar .
