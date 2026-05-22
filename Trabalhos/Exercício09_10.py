#Crie uma função chamada contar_caracteres que receba uma string e um
#caractere como parâmetros e retorne o número de vezes que o caractere
#aparece na string

def contar_caracteres(texto, carect):
    return texto.count(carect)

print(contar_caracteres("banana", "a"))
