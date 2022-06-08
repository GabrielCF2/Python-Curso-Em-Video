#Escreva um programa que receba uma temperatura em ºC e converta ela em ºF
c=float(input("Digite o valor da temperatura "))
f=(c*(9/5))+32
print("A temperatura de {:.1f}ºC é igual a {:.1f}ºF".format(c,f))