"""
Escribe este código:
Imaginemos un sistema de votación en el que varios votantes pueden emitir votos para diferentes opciones.
Tenemos 2 variables globales:
Candidato A
Candidato B
Tu programa principal llamara a una función llamada votación.

En la función votación:
Haces un random para votar A o B
Si ha salido A --> Incrementas en 1 el valor de la variable global Candidato A e imprimes un mensaje parecido a este "Soy el votante 1 y he votado A"
Si ha salido B --> Incrementas en 1 el valor de la variable global Candidato B e imprimes un mensaje parecido a este "Soy el votante 1 y he votado B"
En el programa principal imprimes:
Han votado 1 persona
El total de votos para A es:
El total de votos para B es:

Ejercicio a entregar:
Pasa este código a Threads i pon 10 votantes. los mensajes que imprimen la función votación y el programa principal cambian:

Función votación: "Soy el votante (número de iteración)  y he votado A"
Función main hace un bucle y crea 10 Threads. Por ello debería acabar diciendo que han votado 10 personas y decir cómo han quedado las votaciones.

Utiliza join() para que los mensajes del programa principal se impriman al final.
"""
import random
import threading
import time

candidato_a = 0
candidato_b = 0


def votacion(hilo):
    global candidato_a, candidato_b
    voto = random.randint(0, 1)

    if voto == 1:
        candidato_a += 1
        print(f"Soy el votante {hilo} y he votado A")
    else:
        candidato_b += 1
        print(f"Soy el votante {hilo} y he votado a B")


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
