numeros_encontrados = []

for numero in range(1000, 2001):
    if numero % 11 == 5:
        numeros_encontrados.append(numero)

print(f"divi: {numeros_encontrados}")