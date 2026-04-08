valor = int(input("Digite a sua nota: "))
while valor < 0 or valor > 10:
    print("Nota invalida")
    valor = int(input("Digite uma nota valida:"))

print("OK")