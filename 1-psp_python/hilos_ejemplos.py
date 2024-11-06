import threading
import time
import random

# Creamos una tarea para dale a los hilos


def tarea_hilo(identificador):
    tiempo_espera = random.randint(1, 5)
    time.sleep(tiempo_espera)
    print(f"Hilo {identificador} ejecutando y he dormido {tiempo_espera}")


if __name__ == "__main__":

    hilos = []

    for i in range(10):
        nuevo_hilo = threading.Thread(
            target=tarea_hilo, args=(i,))
        hilos.append(nuevo_hilo)
        nuevo_hilo.start()

    for j in range(10):
        print("Soy el hilo principal y estoy en la vuelta del bucle ", j)
        time.sleep(1)
    # join hace que haste que ese hilo no se ejecute no sigue el programa.
    for hilo in hilos:
        hilo.join()

print("Fin del programa")
