import threading
import time


def tarea_animal(nombre, patas, vuela):
    vuelo = "vuela" if vuela else "no vuela"
    informacion = f"{nombre} es un animal con {patas} patas y {vuelo}."
    print(informacion)

# Desarrollar el método principal para ejecutar la tarea anterior con un hilo para cada animal, se deben crear, iniciar y esperar a que terminen todos los hilos. Se deben utilizar bucles y listas para solucionar el ejercicio.
# Listas a utilizar


animales = ["Perro", "Pájaro", "Araña"]
patas = [4, 2, 8]
vuela = [False, True, False]

if __name__ == "__main__":
    hilos = []
    for i in range(len(animales)):
        nuevo_hilo = threading.Thread(
            target=tarea_animal, args=(animales[i], patas[i], vuela[i],))
        hilos.append(nuevo_hilo)
        nuevo_hilo.start()
    for hilo in hilos:
        hilo.join()

    print("Programa terminado")
