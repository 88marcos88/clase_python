"""
Intenta hacer el Ejercicio opcional 1 con Threads

En el ejercicio opcional 1 se pide:
Dada una frase que te pase el usuario, tu programa debe realizar el recuento de vocales de dicha frase.

Haz que se ejecute 3 veces de forma paralela.

*Si pones sleep de forma random en el código del hilo, verás que lío de frases y resultados somriure
tiempo_espera = random.randint(1, 5)
time.sleep(tiempo_espera)
"""

import threading
import random
import time


def contVocales(frase):

    vocales = "aeiou"
    contador = 0

    for char in frase:
        if char.lower() in vocales:
            contador += 1
    tiempo_espera = random.randint(1, 5)
    time.sleep(tiempo_espera)

    print(f"{threading.current_thread().name} terminado. Tu palabra {
          frase} tiene: {contador} vocales y espero: {tiempo_espera} segundos")


if __name__ == "__main__":

    hilos = []
    frases = []

    for i in range(3):
        frase = input("Introduce una frase: ")
        frases.append(frase)

    for hilo in range(3):
        nuevo_hilo = threading.Thread(
            target=contVocales, args=(frases[hilo],), name=f"hilo-{hilo}")
        hilos.append(nuevo_hilo)
        nuevo_hilo.start()

    for hilo in hilos:
        hilo.join()

print("Fin del programa")
