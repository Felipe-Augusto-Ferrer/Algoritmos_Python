print()
print("Digite qual das operações matemáticas deseja realizar:") #soma,subt,mult,divi,sair
while True:
    print("1:Soma")
    print("2:Subtracao")
    print("3:Multiplicação")
    print("4:Divisão")
    print("0:Sair")
    op=int(input("Operação:"))

    if op==0:
        print("Saindo...")
        break

    if op == 1 or op == 2 or op == 3 or op == 4: 
        n1=int(input("Primeiro número: "))
        n2=int(input("Segundo número: "))
    else:
        print("Valor inválido")
        print()

    if op==1:
        print(f"\n{n1} + {n2} = {n1 + n2}\n") #\n para pular linha
    elif op==2:
        print(f"\n{n1} - {n2} = {n1 - n2}\n")
    elif op==3:
        print(f"\n{n1} * {n2} = {n1 * n2}\n")
    elif op==4:
        if n2 != 0:
            print(f"\n{n1} / {n2} = {n1/n2}\n")
        else:
            print("\nDivisão por zero\n")