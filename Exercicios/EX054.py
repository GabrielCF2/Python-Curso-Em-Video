#Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
#mostre quantas pessoas ainda não atigiram a maioridade e quantos já são maiores.
from datetime import date
ad = 0
cri = 0
ano = date.today().year
for c in range(0,7):
    n=int(input("Digite o ano de nascimento da pessoa: "))
    n=ano-n
    if n >=21:
        ad+=1
    else:
        cri+=1
print("{} pessoas já atingiram a maioridade, e {} pessoas ainda são menores de idade.".format(ad,cri))