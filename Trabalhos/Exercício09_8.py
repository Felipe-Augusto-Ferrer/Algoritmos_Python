#Crie uma função chamada e_palindromo que receba uma string como
#parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás
#para frente for igual à original) e False caso contrário.

def e_palindrmo(palavra):
    n=palavra.lower()
    inverso = n[::-1]
    if n == inverso:
        return True
    else:
        return False

print(e_palindrmo("ovo"))