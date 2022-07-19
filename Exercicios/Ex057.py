#Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'.
#Caso esteja errado faça a digitação novamente até ter um valor correto.
sexo = str(input("Digite o seu sexo: ")).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f"Você digitou {sexo}, que é um valor inválido, digite novamene: ").upper())
print(f"Você escolheu o sexo {sexo}.")