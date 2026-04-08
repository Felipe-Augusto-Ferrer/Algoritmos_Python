x=float(input("Digite a coordenada x: "))
y=float(input("Digite a coordenada y: "))
if 0<x<10 and 0<y<10 or 0<x<10 and y==0 or x==0 and 0<y<10:
    print("Está dentro do quadrado")
elif x==0 and y==0 :
    print("Está na fronteira")
else:
    print("Fora do quadrado")