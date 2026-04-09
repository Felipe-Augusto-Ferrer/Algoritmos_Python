# while True:
#     palavra=input("Digite uma palavra que começe com uma vogal: ").lower()
#     if palavra[0] in 'aeiou':
#         break
#     else:
#         print("Deu ruim")
# for letra in palavra:
#     print (letra)

palavra = input("Palavra: ")

while palavra[0].lower() != 'a' and palavra[0].lower() != 'e' and palavra[0].lower() != 'i' and palavra[0].lower() != 'o' and palavra[0].lower() != 'u':
    print("Palavra inválida")
    palavra=input("Palavra: ")

for letra in palavra:
    print(letra)
