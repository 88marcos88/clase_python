"""
Ejercicio opcional 5:

Necesitaremos un hilo principal que creará mediante bucles, 5 threads (hilos secundarios) que llamarán a una función para
dividir y otros 5 threads a una función para multiplicar. Crearemos una variable a la cual asignaremos un número aleatorio
entre el 20 y el 100, esta variable será el argumento para todos los hilos.

Los threads de la función dividir, dividirán el número que les llegue por el argumento entre 2 e imprimirán:
“Soy el thread con nombre …. . Mi identificador es: …  y el resultado del número dividido es: ….”.
Se les cambiará el nombre usando la instancia de la clase Thread y yendo a su argumento directamente
(posteriormente a ser creados): HiloDiv1, HiloDiv2...
A los threads de la función multiplicar se les cambiará el nombre: HiloMulti6, HiloMulti7, HiloMulti8, HiloMulti9 y HiloMulti10,
en la propia creación del thread. Estos threads multiplicarán el número del argumento por 2 e imprimirán: “Soy el thread …. .
Mi identificador es: …. y el resultado de la multiplicación es: …

"""
import threading
import time
import random


def dividir(n1, n2):

    try:
        print(f"Soy el thread con nombre {threading.current_thread().name} Mi identificador es: {
              threading.current_thread().ident} El resultado de dividir {n1}/{n2} es: " + str(n1/n2))
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operacion erronea"


def multi(n1, n2):
    print(f"Soy el thread con nombre {threading.current_thread().name} Mi identificador es: {
          threading.current_thread().ident} El resultado de multiplicar {n1}*{n2} es: " + str(n1*n2))


if __name__ == "__main__":

    hilos = []

    for i in range(10):
        if i < 5:
            rand = random.randint(20, 100)
            nuevo_hilo = threading.Thread(target=dividir, args=(rand, 2,))
            nuevo_hilo.name = f"HiloDiv{i}"
            hilos.append(nuevo_hilo)
            nuevo_hilo.start()
        else:
            rand = random.randint(20, 100)
            nuevo_hilo = threading.Thread(
                target=multi, args=(rand, 2,), name=f"HiloMulti{i}")
            hilos.append(nuevo_hilo)
            nuevo_hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Programa terminado")
