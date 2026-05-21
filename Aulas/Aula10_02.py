sorteados=[17,19,27,32,38,44]
apostados=[0,1,2,3,4,5]
acertos = 0
for i in range (6):
    n=int(input("Digite o seu número: "))
    apostados[i] = n
    if n == sorteados[i]:
        acertos += 1

print()
print(f"Números apostados: {apostados}")
print(f"Números sorteados: {sorteados}")
print(f"Acertos: {acertos}")