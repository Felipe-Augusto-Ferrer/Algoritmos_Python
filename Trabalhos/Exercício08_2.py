#Prática 2
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

print(matriz)
print()
for linha in range(3):
    print(matriz[linha])
print()
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])

print()
#Prática 3
soma = matriz[0][0] + matriz[1][0]
subt = matriz[2][2] - matriz[2][1]
mult = matriz[0][1] * matriz[2][0]
divi = matriz[1][2] / matriz[0][2]

print(f"{matriz[0][0]} + {matriz[1][0]} = {soma}")
print(f"{matriz[2][2]} - {matriz[2][1]} = {subt}")
print(f"{matriz[0][1]} * {matriz[2][0]} = {mult}")
print(f"{matriz[1][2]} / {matriz[0][2]} = {divi}")

