# 1
A=[1,0,5,-2,-5,7]
soma1=A[0]+A[1]+A[5]
print(f"A soma dos vetores é: {soma1}")
print()
A[4]=100

print("Vetor A:")
for numero in A:
    print(numero)

# 2
print("=============")
print("2:")
indice2=0
valores2=[0,1,2,3,4,5]
for n in valores2:
    numeros2=int(input("Digite um número: "))
    valores2[indice2]=numeros2
    indice2=indice2+1

print(f"Valores lidos: {valores2}")

# 3
print("=============")
print("3:")
indice3=0
vetor3=[0,1,2,3,4,5,6,7,8,9]
vetor3=[0,1,2,3,4,5,6,7,8,9]
for n in vetor3:
    numeros3=int(input("Digite um número: "))
    vetor3[indice3]=numeros3
    quadrado=vetor3[indice3]*vetor3[indice3]
    vetor3[indice3]=quadrado
    indice3 += 1

print(f"Lista 1: {vetor3}")
print(f"Quadrado da lista 1: {vetor3}")

# 4
print("=============")
print("4:")
vetor4 = [0,1,2,3,4,5,6,7]
for i in vetor4:
    numeros4 = int(input("Digite um número: "))
    vetor4[i]=numeros4

print()
print(vetor4)
X=int(input("Digite um número Y correspondente a uma posição da lista (0 à 7): "))
Y=int(input("Digite um número X correspondente a uma posição da lista (0 à 7): "))

soma4 = vetor4[X] + vetor4[Y]

print(f"Soma dos vetores: {vetor4[X]} + {vetor4[Y]} = {soma4}")

# 5
print("=============")
print("5:")
vetor5 = [0,1,2,3,4,5,6,7,8,9]
par = 0
for i in vetor5:
    numeros5 = int(input("Digite um número: "))
    vetor5[i]=numeros5
print("=============")
print("números pares:")
for numero in vetor5:
    if numero%2==0:
        print(numero)
        par += 1

# 6
print("=============")
print("6:")
vetor6 = [0,1,2,3,4,5,6,7,8,9]
for i in vetor6:
    numeros6 = int(input("Digite um número: "))
    vetor6[i]=numeros6

print(f"Valor máximo: {max(vetor6)}")
print(f"Valor mínimo: {min(vetor6)}")

#7
print("=============")
print("7:")
vetor7 = [0,1,2,3,4,5,6,7,8,9]
for i in vetor7:
    numeros7 = int(input("Digite um número: "))
    vetor7[i]=numeros7
print(vetor7)
max = max(vetor7)
print(f"valor mínimo: {max}")
print(f"índice: {vetor7.index(max)}")

#8
print("=============")
print("8:")
prova=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
soma=0
for i in prova:
    nota=int(input(f"Digite a nota do aluno {i}: "))
    soma+=nota

media=soma/15

print(f"A média da sala é : {media:.2f}")

#9
print("=============")
print("9:")
vetor9 = [0,1,2,3,4,5,6,7,8,9]
positivo = 0
negativo = 0
for i in vetor9:
    numeros9 = float(input("Digite um número positivo ou negativo: "))
    vetor9[i]=numeros9
print("=============")
print("números positivos:")
for numero in vetor9:
    if numero>0:
        print(numero)
        positivo += 1
print("=============")
print("números negativos:")
for numero in vetor9:
    if numero<0:
        print(numero)
        negativo += 1

# 10
print("=============")
print("10:")
vetor10=[0,1,2,3,4]
soma = 0
for i in vetor10:
    numero10=int(input("Digite um número:"))
    vetor10[i]=numero10
    soma +=numero10
print(numero10)
print(f"Valor máximo: {max(vetor10)}")
print(f"Valor mínimo: {min(vetor10)}")
print(f"Soma: {soma}")

# 11
print("=============")
print("11:")
vetor11=[0,1,2,3,4]
for i in vetor11:
    numero11=int(input("Digite um número:"))
    vetor11[i]=numero11
maximo10 = max(vetor11)
minimo10 = min(vetor11)
print(f"Índice do máximo: {vetor11.index(maximo10)}")
print(f"Índici do mínimo: {vetor11.index(minimo10)}")
