numero = int(input("digite o numero: "))

print('---SOLUÇÃO COM FOR----')

for m in range(1,11):
    resultado = numero * m
    print(f"{numero} x {m}= {resultado}")


print('---SOLUÇÃO COM WHILE----')
ciclos = 1 
while ciclos <= 10:
    resultado = numero * ciclos
    print(f"{numero} x {m}= {resultado}")



