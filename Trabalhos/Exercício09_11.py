# Implemente uma calculadora simples em Python utilizando funções. A
# calculadora deve ser capaz de realizar as seguintes operações
# matemáticas básicas:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão
# Requisitos:
# • Crie uma função para cada operação matemática (soma,
# #subtração, multiplicação e divisão). As funções devem receber
# dois valores e retornar o resultado da operação.
# • Implemente uma função para exibir o menu de opções para o
# usuário.
# • O programa deve repetir o menu após cada operação, até que
# o usuário escolha a opção de sair.

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def menu():
    print("="*20)
    print("      CALCULADORA      ")
    print("="*20)
    print("Soma(1)")
    print("Subtração(2)")
    print("Multiplicação(3)")
    print("Divisão(4)")
    print("Sair(5)")
    print("="*20)

def main():
    while True:
        menu()

        opcao=int(input("Digite opção:"))

        if opcao=="5":
            print("Encerrando...")
            break

        if opcao=="1":   
            soma(n1,n2)

        elif opcao=="2":
            subtracao(n1,n2)

        elif opcao=="3":
            multiplicacao(n1,n2)

        elif opcao=="4":
            subtracao(n1,n2)




