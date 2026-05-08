import random

numerosJogador1=[]
numerosJogador2=[]

for i in range(3):
    numerosJogador1.append(random.randint(1,6))
    numerosJogador2.append(random.randint(1, 6))

soma1=sum(numerosJogador1)
soma2=sum(numerosJogador2)
print(f"O jogador 1 teve os seguintes valores {numerosJogador1}")
print(f"O jogador 2 teve os seguintes valores {numerosJogador2}")
print()
print(f"A soma do jogador 1 é: {soma1}")
print(f"A soma do jogador 2 é: {soma2}")
if soma1 > soma2:
    print("\nJogador 1 vence!")
if soma2 > soma1:
    print("\nJogador 2 vence!")