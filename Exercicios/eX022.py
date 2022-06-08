#Crie um programa que leia o nome comleto de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas e minúsculas.
#-Quantas letras tem ao todo (sem considerar os espaços)
#-Quantas letras tem o primeiro nome


nome=str(input("Digite o seu nome completo: ")).strip()
print("O seu nome em maiúsculo é {}".format(nome.upper()))
print("O seu nome em minúsculo é {}".format(nome.lower()))

nome_separado = nome.split()
quant_letras = len(nome)-nome.count(" ")
print("Seu nome tem {} letras".format(quant_letras))

quant_prim = nome_separado[0]
print("O primeiro nome tem {} letras".format(len(quant_prim)))