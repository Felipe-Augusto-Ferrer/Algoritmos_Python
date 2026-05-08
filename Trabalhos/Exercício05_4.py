n=int(input("Digite quantas linhas deseja criar: "))
for linhas in range(1,n+1):
    for linhas2 in range(1,linhas+1):
        print(linhas2,end=" ")
    print()