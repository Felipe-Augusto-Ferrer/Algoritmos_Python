numero = int(input("Digite um número para fazer a média e '-1' para parar: "))

contador = 0
soma = 0
while True:
    soma = soma + numero
    contador += 1

    numero = int(input("Digite outro número: "))
    if numero == -1:
        break

if soma > 0:
    media= soma / contador
    print(f"A média dos números é igual a {media}")

else:
    print("Número invalido")