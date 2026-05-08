lista=[]
n=int(input("Digite um número positivo e inteiro qualquer: "))
lista.append(n)

for i in range(4):
    n=int(input("Digite outro número positivo e inteiro qualquer: "))
    lista.append(n)
print()
#Lista 1
print(f"Lista 1: {lista}")
print()

lista2=sorted(lista)
print(f"Lista ordenada: {lista2}")
print()

lista3=list(reversed(lista2))
print(f"Lista ordenada reversa: {lista3}")
print()

print(f"Tamanho da lista: {len(lista)}")
print(f"Valor máximo: {max(lista)}")
print(f"Valor mínimo: {min(lista)}")
print(f"Soma: {sum(lista)}")




