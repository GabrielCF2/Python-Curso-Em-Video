# Faça um programa que leia um número qualquer e mostre o seu fatorial
n = int(input("Digite um número para descobrir o seu fatorial: "))
c = n
while n>1:
    n=n-1
    c = (c*n)
print(f"O fatorial é {c}.")