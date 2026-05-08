numeros=[5,7,12,2,9,21]
numeros[1]=17
numeros[3]=22
numeros[2]=1
numeros[4]=2

print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])
print(numeros)

print("===========")

#soma 21 e 29
soma = numeros[5]+numeros[4]
print(f"{numeros[5]}+{numeros[4]}={soma}")
#subtração 22 e 17
subt = numeros[3]-numeros[1]
print(f"{numeros[3]}-{numeros[1]}={subt}")
#multiplicação indices 0 e 5
multi = numeros[0]*numeros[5]
print(f"{numeros[0]}X{numeros[5]}={multi}")
#divisão indices 3 e 2
divi = numeros[3]/numeros[2]
print(f"{numeros[3]}/{numeros[2]}={divi}")

print("===========")
#while indice x2
indice=0
while indice<6:
    print(numeros[indice]*2)
    indice+=1


