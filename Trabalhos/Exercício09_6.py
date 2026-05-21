#Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho
#3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal.

def imprime_diagonal(matriz):
    for linha in range(3):
        for coluna in range(3):
            if linha==coluna:
                print(matriz[linha][coluna])

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
imprime_diagonal(matriz2)
            