print("Bla bla bla")
caminho1 = str(input("Qual caminho você vai seguir?(esquerda/direita) ")).lower()
if caminho1 == "esquerda":
    rio= int(input("Você encontrou um rio! Você vai atravessar(1) ou voltar(2)?"))
    if rio == 1:
        print("Você chegou em uma vila segura!")
    elif rio == 2:
        print("Você se perdeu!")
elif caminho1 == "direita":
    montanha=int(input("Você encontrou uma montanha,você irá subir(1) ou voltar(2)"))
    if montanha == 1:
        print("Você encontrou um tesouro!!")
    elif montanha == 2:
        print("Você se perdeu :(")