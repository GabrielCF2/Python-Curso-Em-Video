#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero=int(input("Digite um número de 0 a 9999: "))
mil = numero//1000
cem=numero//100 %10
dez=numero//10 % 10
um=numero//1 % 10
print("Esse número tem {} unidades de milhar, {} centenas, {} dezenas e {} unidades.".format(mil,cem,dez,um))