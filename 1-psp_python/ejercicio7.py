"""
Dado el código del ejercicio anterior, protege la zona crítica con lock().
Debes capturar las excepciones con try, except y finally 
"""
import random
import threading
import time

candidato_a = 0
candidato_b = 0
lock = threading.Lock()


def votacion(hilo):
    global candidato_a, candidato_b
    voto = random.randint(0, 1)

    try:
        lock.acquire
        if voto == 1:
            candidato_a += 1
            print(f"Soy el votante {hilo} y he votado A")
        else:
            candidato_b += 1
            print(f"Soy el votante {hilo} y he votado a B")
    except Exception as e:
        print(f"Ha ocurrido un error en el votante {hilo}: {e}")
    finally:
        lock.release


if __name__ == "__main__":

    hilos = []

    for i in range(10):
        nuevo_hilo = threading.Thread(target=votacion, args=(i,))
        hilos.append(nuevo_hilo)
        nuevo_hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"Han votado: {candidato_a + candidato_b} personas")

    print(f"El total de votos para A es: {candidato_a}")
    print(f"El total de votos para B es: {candidato_b}")
