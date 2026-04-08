usuario=input("Digite o seu usuário: ")
if usuario=="admin":
    senha=input("Digite a sua senha: ")
    if senha=="1234":
        print("Bem-vindo!")
    else :
        print("Bloqueado!!")
elif usuario=="convidado":
    print("Acesso restrito")
else:
    print("Usuário não encontrado")