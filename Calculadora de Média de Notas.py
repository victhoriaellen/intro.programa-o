def calcular_media_notas():
    print("Digite as notas do aluno (digite -1 para encerrar):")
    
    notas = []
    
    while True:
        try:
            nota = float(input("Digite uma nota: "))
            if nota == -1:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média das notas: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida.")

calcular_media_notas()
