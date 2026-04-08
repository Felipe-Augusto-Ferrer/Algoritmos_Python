par=0
impar=0
contador = 0
while contador <= 10:
    n= int(input("Digite um número do teclado: "))
    if n%2==0:
        par += 1
    else:
        impar += 1

    contador += 1
    if contador == 10:
        break

print()
print(f"São {par} números pares e {impar} números ímpares")