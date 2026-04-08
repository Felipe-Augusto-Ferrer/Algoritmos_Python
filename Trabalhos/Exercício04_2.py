n = int(input("Digite um número para fazer a somatória a partir do 1: "))
while n<1:
    n=int(input("Digite um número valido "))

contador = 1
soma = 0
while contador <= n:
    soma = soma + contador
    contador += 1
print(f"A somas dos números até {n} é igual a {soma}")


