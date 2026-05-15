matriz=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
maior_nota = 0
matricula_maior_nota = 0

for linha in range (5):
    print(f"\nDigite os dados do {linha + 1}º aluno:")

    matriz[linha][0] = int(input("Número de matrícula: "))

    matriz[linha][1] = int(input("Média das provas (inteiro): "))

    matriz[linha][2] = int(input("Média dos trabalhos (inteiro): "))

    matriz[linha][3] = matriz[linha][1] + matriz[linha][2] / 2

    if matriz[linha][3] > maior_nota:
        maior_nota = matriz[linha][3]
        matricula_maior_nota = matriz[linha][0]

for linha in range(5):
        print(matriz[linha])
print(f"\n> O aluno com a maior nota final é o de Matrícula: {matricula_maior_nota} (Nota: {maior_nota})")