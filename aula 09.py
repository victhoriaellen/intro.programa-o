import time
for numero in range(1000, 2001):
    if numero % 11 == 5:
        print(f"numero é: {numero}")
        time.sleep(1)

numero = 1000

while numero <= 2000:
    if numero % 11 == 5:
        print(f'o numero é {numero}')
