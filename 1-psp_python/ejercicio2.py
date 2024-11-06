"""
Tomando como base el ejercicio opcional 1, se propone hacer una ampliación. Ahora las frases
no las introduce el usuario directamente, están escritas en un fichero de texto.
Tu programa debe leer línea a línea las frases y contar las vocales. En un fichero “nuevo” de
salida debe indicar:
Frase 1: 8 vocales
Frase 2: 5 vocales
Frase 3: 10 vocales
Crea un fichero de texto (.txt) con tres frases que te gusten y analízalas con tu programa.
"""
vocales = "aeiou"
contador = 0
with open("frases.txt", "w", encoding="utf8") as txt:

    for i in range(3):
        frase = input(f"Introduce la frase {i+1}: ")
        txt.write(frase + "\n")

with open("frases.txt", "r", encoding="utf8") as txt2:
    for linea in txt2:
        for i in linea:
            if i.lower() in vocales:
                contador += 1
        print(f"la frase {linea.strip()} tiene {contador} vocales")
        contador = 0
