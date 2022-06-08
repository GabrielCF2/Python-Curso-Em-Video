#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
# print(junto)
# print(inverso)
if junto == inverso:
    print("A frase digitada é um palíndromo.")
else:
    print("A frase digitada NÃO é um palíndromo.")