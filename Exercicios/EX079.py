#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista.
# Caso o número já exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = []
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print(f"Número {n} adicionado com sucesso.")
    else:
        print("Esse valor já foi inserido anteriormente.")
    r = str(input("Quer continuar? [S/N] "))
    if r in 'Nn':
        break
numeros.sort()
print("-="*30)
print(f"Você digitou os valores {numeros}.")
    