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

candidato_a = 0
candidato_b = 0
