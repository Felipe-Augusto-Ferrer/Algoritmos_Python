contador = 0
for i in range(1,100):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        contador+=1
print(f"\n{contador} números são multiplos de 3 e não multiplos de 5")