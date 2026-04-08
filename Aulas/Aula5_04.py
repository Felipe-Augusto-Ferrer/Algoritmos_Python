palavra = input("Palavra: ")
tamanho = len(palavra)

while tamanho < 3 or tamanho > 10:
    print("Invalido")
    palavra = input("Palavra: ")

print(palavra, len(palavra))