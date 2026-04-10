n1=int(input("Digite a tabuada que quer começar: "))
n2=int(input("Digite a tabuada que quer parar: "))

# for i in range(1,11):
#     resultado= n1*i
#     print(f"{n1} x {i} = {resultado}")

for tabuada in range(n1,n2+1):
    print()
    for j in range(1, 11):
        resultado= tabuada*j
        print(f"{tabuada} x {j} = {resultado}")


    # resultado= n1*i
    # while n1>=n2:
    #     print(f"{n1} x {i} = {resultado}")
    #     n1 += 1