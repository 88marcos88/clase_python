""" 
Semáforos:

Crea un programa que controla la entrada a una frutería.
Dentro de la frutería sólo caben 4 personas.
Crea 10 threads que quieren comprar fruta.

Muestra por pantalla los mensajes a medida que entran las personas:
Está esperando la persona (pon el número)
Está atendida a la persona (pon el número)
Sale de la frutería la persona (pon el número)
"""


import threading
import time
import random

semaforo_fruteria = threading.Semaphore(4)
comprando = random.randint(1, 3)


def entradaFruteria(hilo):
    print(f"Está esperando la persona {hilo}")
    semaforo_fruteria.acquire()
    print(f"Está atendida a la persona {hilo}")
    time.sleep(comprando)
    semaforo_fruteria.release()
    print(f"Sale de la fruteria la persona {hilo}")


if __name__ == "__main__":

    personas = []

    for i in range(10):
        persona = threading.Thread(target=entradaFruteria, args=(i,))
        personas.append(persona)
        persona.start()

    for persona in personas:
        persona.join()

    print("Todas las personas han sido atendidas")
