matriz=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]


for linha in range (4):
    for coluna in range (4):
        n=int(input(f"{linha}x{coluna}: "))
        matriz[linha][coluna]=n

for i in range(4):
        print(matriz[i])