salario = float(input("Digite o seu salário mensal: R$ "))

if salario <= 2000:
    imposto = 0
    print("Isento de imposto de renda5")
elif salario <= 3500:
    imposto = (salario - 2000) * 0.10
    print(f"Imposto de renda: R$ {imposto:.2f}")
else:
    imposto = (1500 * 0.10) + ((salario - 3500) * 0.15)
    print(f"Imposto de renda: R$ {imposto:.2f}")
