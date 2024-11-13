""" 
Productor - Consumidor:

Basándote en el ejercicio de la teoría amplía el programa de esta forma:

Pon 2 productores:

Productor 1: Añade frutas (está especializado en fruta)
Productor 2: Añade verduras
Tienes 2 consumidores que irás sacando frutas o verduras, no hace falta controlar esto.

Ve mostrando por pantalla que van haciendo:

Productor 1 introdujo una fruta (si puedes poner el nombre de una fruta mejor)
Productor 2 introdujo una verdura (si puedes poner el nombre de una verdura mejor)
Consumidor 1: Ha sacado de la cesta (pon si es fruta, verdura o el nombre) producto
Consumidor 2: Ha sacado de la cesta (pon si es fruta, verdura o el nombre) producto
Si te apetece pensar un extra (sin obligación de nada), podrías al final indicar cuántas frutas, 
verduras o el nombre de las mismas se ha llevado cada consumidor.
"""


import threading
import time
import random

frutas = ["Peras", "Kiwi", "Melón", "Manzana"]
verduras = ["Tomate", "Aguacate", "Pepino", "Lechuga"]

BUF_SIZE = 10
buffer = [None] * BUF_SIZE

semaforo_productor = threading.Semaphore(BUF_SIZE)
semaforo_consumidor = threading.Semaphore(0)
semaforo_lock = threading.Semaphore(1)
indice_entrada = 0
indice_salida = 0


class ProductorF(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        global buffer, indice_entrada

        for i in range(5):
            item = random.choice(frutas)
            time.sleep(random.randint(1, 3))

            semaforo_productor.acquire()
            semaforo_lock.acquire()

            buffer[indice_entrada] = (item)
            indice_entrada = (indice_entrada + 1) % BUF_SIZE
            print(f"Productor Frutas {self.nombre} introdujo: {item}")

            semaforo_lock.release()
            semaforo_consumidor.release()


class ProductorV(threading.Thread):

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        global buffer, indice_entrada

        for i in range(5):
            item = random.choice(verduras)
            time.sleep(random.randint(1, 3))

            semaforo_productor.acquire()
            semaforo_lock.acquire()

            buffer[indice_entrada] = (item)
            indice_entrada = (indice_entrada + 1) % BUF_SIZE
            print(f"Productor Verduras {self.nombre} introdujo: {item}")

            semaforo_consumidor.release()
            semaforo_lock.release()


class Consumidor(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        global buffer, indice_salida
        for i in range(2):
            time.sleep(random.randint(1, 3))

            semaforo_consumidor.acquire()
            semaforo_lock.acquire()

            item = buffer[indice_salida]
            indice_salida = (indice_salida + 1) % BUF_SIZE
            print(f"El consumidor {self.nombre} ha adquirido {item}")

            semaforo_productor.release()
            semaforo_lock.release()


if __name__ == "__main__":
    productores = []
    clientes = []

    productorFrutas = ProductorF("Paqui")
    productores.append(productorFrutas)
    productorVerduras = ProductorV("Rafa")
    productores.append(productorVerduras)

    cliente1 = Consumidor("Manuel")
    clientes.append(cliente1)
    cliente2 = Consumidor("Sandra")
    clientes.append(cliente2)

    for cliente in clientes:
        cliente.start()

    for productor in productores:
        productor.start()

    for cliente in clientes:
        cliente.join()

    for productor in productores:
        productor.join()
    print("La fruteria ha cerrado")
