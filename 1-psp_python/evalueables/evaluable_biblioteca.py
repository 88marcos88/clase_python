"""
Crea un programa que simule el funcionamiento de una biblioteca. En la biblioteca hay dos tipos de acciones que los usuarios pueden realizar:
tomar un libro prestado o devolver un libro. Hay 10 libros disponibles en la biblioteca al principio del día, y los usuarios pueden hacer cualquiera
de estas dos acciones de manera aleatoria.

El programa debe tener dos variables globales: libros_disponibles y usuarios_prestamos, donde:

libros_disponibles guarda cuántos libros quedan en la biblioteca.
usuarios_prestamos guarda cuántos libros han sido prestados en total durante el día.
Se debe crear una clase base común (Biblioteca) y dos clases específicas que heredarán de ella, la clase ClientePrestamo y
ClienteDevolucion que realizarán un cálculo diferente. Ambas clases simulan la interacción de un usuario con la biblioteca.

Si un usuario toma un libro (ClientePrestamo): La cantidad de libros disponibles disminuye en 1 (si hay libros disponibles).
Si un usuario devuelve un libro (ClienteDevolucion): La cantidad de libros disponibles aumenta en 1 (si el usuario tiene libros prestados).
Se deben crear 15 hilos. Cada hilo representará un usuario que realiza una acción aleatoria (tomar o devolver un libro).

Si el hilo representa a un usuario que toma un libro, ejecutará la clase ClientePrestamo y el nombre del hilo será Hilo_tomar_k
(k empezará en 1 y se incrementará por cada Hilo_tomar_k).
Si el hilo representa a un usuario que devuelve un libro, ejecutará la función ClienteDevolucion y el nombre del hilo será Hilo_devolver_k
(k empezará en 1 y se incrementará por cada Hilo_devolver_k).
Las operaciones críticas deben estar protegidas con un Lock para evitar problemas de concurrencia.
Al final del programa, una vez que todos los usuarios han realizado sus acciones, se debe mostrar la cantidad de libros disponibles en la
biblioteca y el número total de préstamos realizados durante el día.
Implementa una captura de excepciones dentro de los hilos utilizando el bloque with.
Importante: Comentar el código con explicaciones completas sobre que se pretende en cada línea de código.
"""

import threading
import random

lock = threading.Lock()  # Genera el bloqueo de recursos


# La clase biblioteca genera las dos variables globales
class Biblioteca:

    libros_disponibles = 10
    total_prestados = 0
    usuarios_prestados = 0


# La clase que hereda de Biblioteca como pide el enunciado y a su vez de threading para generar la funcion de los hilos
class ClientePrestamo(Biblioteca, threading.Thread):

    clientes = 1  # Contador para asignarle el número al final del nombre

    def run(self):  # El run para ajustar la funcion del hilo
        with lock:  # Bloqueamos los recursos para evitar carrera
            try:
                if Biblioteca.libros_disponibles > 0:  # Solo coge libo si quedan disponibles
                    Biblioteca.libros_disponibles -= 1  # Resta el libro
                    Biblioteca.usuarios_prestados += 1  # Aumenta el contador de préstamos
                    Biblioteca.total_prestados += 1  # Aumentamos el contador de libtos prestados
                    # Asigna el nombre + el número
                    self.name = f"Hilo_tomar_{ClientePrestamo.clientes}"
                    ClientePrestamo.clientes += 1
                    print(f"{self.name} ha tomado un libro. Libros disponibles: {
                          Biblioteca.libros_disponibles}")
                else:
                    self.name = f"Hilo_tomar_{ClientePrestamo.clientes}"
                    print(f"{self.name}: No hay libros disponibles para tomar.")
            except Exception:
                print("Ha ocurrido un error al retirar el libro")


# La clase que hereda de Biblioteca como pide el enunciado y a su vez de threading para generar la funcion de los hilos
class ClienteDevolucion(Biblioteca, threading.Thread):

    clientes = 1  # Contador para asignarle el número al final del nombre

    def run(self):  # El run para ajustar la funcion del hilo
        with lock:  # Bloqueamos los recursos para evitar carrera
            try:
                # Comprueba si hay libros prestados que se puedan devolver
                if Biblioteca.usuarios_prestados > 0:
                    Biblioteca.libros_disponibles += 1  # Suma el libro
                    Biblioteca.usuarios_prestados -= 1  # Decrementa el contador de préstamos
                    # Asigna el nombre + el número
                    self.name = f"Hilo_devolver_{ClienteDevolucion.clientes}"
                    ClienteDevolucion.clientes += 1
                    print(f"{self.name} ha devuelto un libro. Libros disponibles: {
                          Biblioteca.libros_disponibles}")
                else:
                    self.name = f"Hilo_devolver_{ClienteDevolucion.clientes}"
                    print(f"{self.name}: No hay libros en prestamo para devolver.")

            except Exception:
                print("Ha ocurrido un error al retirar el libro")


if __name__ == "__main__":

    hilos = []  # Lista para agregar los hilos

    for i in range(15):
        # Aleatorio para ver si coge o deja libro
        decision = random.randint(1, 2)
        # Para simular que un cliente ya tiene un libro se debe dar la condición de que el aleatorio asigne devolver libro
        # y a su vez "haya un cliente con libro (biblioteca.usuario prestado)"
        if decision == 1 and Biblioteca.usuarios_prestados > 0:
            nuevo_hilo = ClienteDevolucion()
            hilos.append(nuevo_hilo)
            nuevo_hilo.start()
        else:
            nuevo_hilo = ClientePrestamo()
            hilos.append(nuevo_hilo)
            nuevo_hilo.start()

    for hilo in hilos:  # Espera a que todos los hilos terminen
        hilo.join()

    print("\nBiblioteca cerrada")
    print(f"Libros disponibles al final del día: {
          Biblioteca.libros_disponibles}")
    print(f"Total de préstamos realizados durante el día: {
          Biblioteca.total_prestados}")

""" 
Si en vez de poner el nombre de hilo libros tomar/devolver pones persona 1, persona 2 etc, como los contadores no son globales el número de la persona
que devuelve siempre va a ser el número de una persona que antes a cogido pero nunca se repetira ni se duplicara. y da la sensación que el que devuelve
siempre va a ser alguien que antes ha cogido un libro
"""
