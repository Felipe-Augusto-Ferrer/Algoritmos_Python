a=float(input("Digite o lado 'a' da figura(Lado maior):"))
b=float(input("Digite o lado 'b' da figura:"))
c=float(input("Digite o lado 'c' da figura:"))
if a+b>c or a+c>b or b+c>a:
    print("Esta figura pode ser um triângulo.")
    if a==b==c:
        print("E é um triângulo Equilátero.")
    elif a==b or a==c or b==c:
        print("E é um triângulo Escaleno.")
    elif a!=b!=c:
        print("E é um triângulo Isósceles.")
    if a**2==b**2+c**2:
        print("E também é um triângulo retângulo.")
else:
    print("Não é um triângulo")