while True:
    n = int(input("Digite um número inteiro e positivo: "))
    if n > 0:
        break
    else:
        print("Número inválido")

soma = 0
lista=[]
for i in range(1,n+1):
    soma+=i
    lista.append(str(i))
expressao= "+".join(lista)
print(f"{expressao} = {soma}")