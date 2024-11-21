"""
Dado el código del ejercicio anterior, protege la zona crítica con lock().
Debes capturar las excepciones con with

El objeto Lock debe estar en el constructor del la clase Thread.
Cuando ejecute Thread debe hacer lo que antes hacia la función votación. 
"""

import random
import threading

candidato_a = 0
candidato_b = 0


class Votacion(threading.Thread):
    def __init__(self, lock, hilo):
        super().__init__()
        self.lock = lock
        self.hilo = hilo

    def run(self):
        global candidato_a, candidato_b
        voto = random.randint(0, 1)

        try:
            with self.lock:
                if voto == 1:
                    candidato_a += 1
                    print(f"Soy el votante {self.hilo} y he votado A")
                else:
                    candidato_b += 1
                    print(f"Soy el votante {self.hilo} y he votado B")
        except Exception as e:
            print(f"Ha ocurrido un error en el votante {self.hilo}: {e}")


if __name__ == "__main__":

    candidato_a = 0
    candidato_b = 0
    lock = threading.Lock()

    hilos = []

    for i in range(10):
        nuevo_hilo = Votacion(lock, i)
        hilos.append(nuevo_hilo)
        nuevo_hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"Han votado: {candidato_a + candidato_b} personas")

    print(f"El total de votos para A es: {candidato_a}")
    print(f"El total de votos para B es: {candidato_b}")
