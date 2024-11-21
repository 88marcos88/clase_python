"""
Un supermercado tiene 5 cajas disponibles para atender a los clientes.
Cuando un cliente llega al supermercado, pide pasar por una caja. Si hay alguna caja libre,
se le asigna una, en caso contrario deberá esperar en la fila hasta que una caja quede libre.

El supermercado también tiene una promoción en la que ciertos productos tienen un descuento por tiempo limitado.
Para gestionar esto, se utiliza un temporizador (Timer) que activa la promoción cada 10 segundos (tiempo inactiva)
y la desactiva tras 5 segundos (tiempo activa).

Al finalizar la atención de un cliente, este deja libre la caja, permitiendo que otro cliente entre.
Además, una vez que hayan sido atendidos todos los clientes del día, se cierra el supermercado y se espera
 a que todas las cajas hayan terminado de atender para mostrar un mensaje: "El supermercado ha cerrado por hoy".

Requisitos:

Debes utilizar un semáforo para gestionar el acceso a las cajas (con capacidad de 5).
En el supermercado entrarán 15 clientes.
El tiempo de atención al cliente es una espera entre 1 y 3 segundos.
Se deben mostrar mensajes con el número del cliente, cuando espera en la caja,
cuando aprovecha la promoción, cuando está siendo atendido y cuando deja la caja.
Debes usar un temporizador (Timer) para activar y desactivar la promoción de manera periódica.
También es interesante usar Lock() para la variable compartida que controlará si la promoción está activa o no.
Además, necesitaremos dos funciones, una para activar la promoción y otra para desactivarla.
Usa una barrera (Barrier) para asegurarte de que todos los clientes han terminado de ser atendidos
antes de que se muestre el mensaje de cierre del supermercado.
"""

import threading
import random
import time

cajas = threading.Semaphore(5)  # Semaforo imita a las 5 cajas abiertas
lock = threading.Lock()  # Lock para proteger los recursos
promocion = False  # Variable que dice si esta activada la promo
# Barrera para esperar que acaben los procesos e inicie el final del hilo principal
barrera = threading.Barrier(16)
promofin = False  # Boolean para finalizar los Timer y que acabe el programa


def activaPromo():  # Funcion para activar la promo
    global promocion, promofin

    if promofin:  # Finaliza bucle promo
        return

    with lock:  # Bloquea los recursos
        promocion = True  # Activa la promo
        # Timer para activar la funcion de desactivar la promo
        desactivar = threading.Timer(5, desactivarPromo)
        desactivar.start()  # Inicio del timer


def desactivarPromo():  # Funcion para desactivar la promo
    global promocion, promofin

    if promofin:  # Finaliza bucle promo
        return

    with lock:  # bloquea los recursos
        promocion = False  # Desactiva la promo
        # Timer para desactivar la funcion de desactivar la promo
        activar = threading.Timer(10, activaPromo)
        activar.start()  # Inicio del timer


def pasarPorCaja(hilo):

    # Tiempo aleatorio que tada en ser atendido
    tiempoAtencio = random.randint(1, 3)

    try:
        cajas.acquire()  # Adquiere el Semaforo
        print(f"{hilo} esta siendo atendido...")
        time.sleep(tiempoAtencio)
        with (lock):  # Bloquea recursos y al finalizar los desbloquea
            if promocion:
                print(f"{hilo} ya ha sido atendidio con un tiempo de espera de {
                    tiempoAtencio}, ha aprovechado la promoción y deja la caja.")
            else:
                print(f"{hilo} ya ha sido atendidio con un tiempo de espera de {
                    tiempoAtencio}, no ha aprovechado la promoción y deja la caja.")
        cajas.release()  # Libera el semaforo
        barrera.wait()  # Suma a la barrera una iteración
    except Exception:
        print(f"Ha ocurrido un error al atender a {hilo}")


if __name__ == "__main__":

    clientes = []
    activaPromo()

    for i in range(15):

        nuevo_hilo = threading.Thread(
            target=pasarPorCaja, args=(f"Cliente {i + 1}",))
        nuevo_hilo.start()
        clientes.append(nuevo_hilo)

    barrera.wait()
    promofin = True  # Finaliza bucle promo para poder cerrar el programa

    print("\nEl supermercado ha cerrado por hoy")
