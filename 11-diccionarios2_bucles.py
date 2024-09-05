capitales = {"China": "Pekín", "India": "Nueva Delhi",
             "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for key in capitales:
    print(key)
    print(capitales[key])

for clave, valor in capitales.items():
    print()
    print(clave + " -> " + valor)

print(capitales.items())
print("----------------------")
print(capitales)
