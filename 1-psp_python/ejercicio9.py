"""
 Desarrolla un programa en Python que simule un sistema de procesamiento de tareas con múltiples hilos. Se deben crear tres tipos de hilos 
 que simulen tres tipos de procesos: Proceso A, Proceso B y Proceso C.

Cada tipo de proceso debe realizar un cálculo diferente en un bucle de 5 iteraciones, ese cálculo puede ser un time.sleep(un tiempo pequeño aleatorio)
y debe heredar de una clase base común.
Se debe sincronizar el acceso a una variable compartida (por ejemplo, un contador de tareas completadas cada vez que se haga un cálculo, 
que equivale a cada iteración del bucle anterior) usando un Lock.
Los hilos deben manejar excepciones utilizando la cláusula with y mostrar un mensaje si ocurre un error durante su ejecución.
Todos los hilos deben ser ejecutados simultáneamente y el programa principal debe esperar a que todos terminen usando join().
Requisitos:
Debe haber un total de 5 hilos en ejecución (por ejemplo, 2 del tipo A, 2 del tipo B y 1 del tipo C).
Cada hilo debe realizar su cálculo en un bucle de 5 iteraciones.
Utiliza lock para evitar que varios hilos accedan a la vez a la variable compartida.
Implementa una captura de excepciones dentro de los hilos utilizando el bloque with.

"""

import threading
import random
import time

tareas = 0
lock = threading.Lock()


class ProcesoBase(threading.Thread):
    def __init__(self, hilo):
        super().__init__()
        self.hilo = hilo
        self.lock = lock

    def run(self):
        global tareas
        try:
            for i in range(5):
                self.calculo(i)
                with self.lock:
                    tareas += 1
        except Exception:
            print("Ha ocurrido un error ")

    def calculo(self, iter):
        raise NotImplementedError("Implementar en subcalss")


class ProcesoA(ProcesoBase):

    def calculo(self, iter):
        tiempo = random.randint(1, 5)
        time.sleep(tiempo)
        print(f"{self.hilo} del proceso A, Estoy en la iteracion {
              iter}: Duración {tiempo} segundos")


class ProcesoB(ProcesoBase):

    def calculo(self, iter):
        tiempo = random.randint(1, 5)
        time.sleep(tiempo)
        print(f"{self.hilo} del proceso B, Estoy en la iteracion {
              iter}: Duración {tiempo} segundos")


class ProcesoC(ProcesoBase):

    def calculo(self, iter):
        tiempo = random.randint(1, 5)
        time.sleep(tiempo)
        print(f"{self.hilo} del proceso C, Estoy en la iteracion {
              iter}: Duración {tiempo} segundos")


if __name__ == "__main__":

    hilos = [
        ProcesoA("Hilo 1"),
        ProcesoA("Hilo 2"),
        ProcesoB("Hilo 3"),
        ProcesoB("Hilo 4"),
        ProcesoC("Hilo 5")
    ]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"Fin del programa tareas realizadas {tareas} ")
