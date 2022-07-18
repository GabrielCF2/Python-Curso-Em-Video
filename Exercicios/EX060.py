# Faça um programa que leia um número qualquer e mostre o seu fatorial
n = int(input("Digite um número para descobrir o seu fatorial: "))
c = n
cont = 0
while n>1:
    n=n-1
    cont = (c*n)
    c = cont
print(f"O fatorial é {cont}.")