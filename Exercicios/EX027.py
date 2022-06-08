#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome=str(input("Digite o seu nome completo: "))
quant_nome = nome.split()
print("O primeiro nome é {}.".format(quant_nome[0]))
print("E o último nome é {}.".format(quant_nome[len(quant_nome)-1]))
