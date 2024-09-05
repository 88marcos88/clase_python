import csv

with open('ejemplo.csv', newline='', encoding='utf8') as archivo:

    data = csv.reader(archivo, delimiter=',')

    for row in data:
        print(', ' .join(row))
