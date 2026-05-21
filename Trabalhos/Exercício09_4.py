# Escreva uma função chamada "media" que receba uma lista de números como
# parâmetro e retorne a média desses números.
def media():
    lista= []
    for i in range(5):
        n=int(input("Digite um número para a lista"))
        lista.append(n)
    print(lista)

    return lista

media()