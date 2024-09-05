# Genera una lista y trabaja con ella en F.I.F.O, L.I.F.O(last in firt out) o
# Priority

import queue

# FIFO

miCola = queue.Queue()

# Agregar elementos a la cola

miCola.put("Valencia")
miCola.put("Castellón")
miCola.put("Alicante")

# Sacar elementos

print(miCola.get())
print("Siguiente elemento:")

# Sacarlos con bucle

for elemento in miCola.queue:
    print(elemento)


# L.I.F.O
print("---------------------")
miCola2 = queue.LifoQueue()

# Agregar elementos a la cola

miCola2.put("Valencia")
miCola2.put("Castellón")
miCola2.put("Alicante")

# Tamaño cola
print(miCola2.qsize())


for i in range(0, miCola2.qsize()):
    print(miCola2.get())

# Priority
print("---------------------")

miCola3 = queue.PriorityQueue(3)

miCola3.put((2, "Castellón"))
miCola3.put((1, "Valencia"))
miCola3.put((3, "Alicante"))

print("Mi cola esta llena: " + str(miCola3.full()))

print(miCola3.get())
print(miCola3.get())
print(miCola3.get())
