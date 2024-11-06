""" 
Dada una frase que te pase el usuario, tu programa debe realizar el recuento de vocales de
dicha frase.
"""

vocales = "aeiou"
frase = input("Introduce una palabra o frase: ")
contador = 0

for i in frase:
    if i.lower() in vocales:
        contador += 1

print(contador)
