#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso dos lidos.
maior = 0
menor = 0
for c in range(0,5):
    n = float(input("Digite o peso da pessoa: "))
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print("O menor peso foi de {:.3f}Kg e o maior peso foi de {:.3f}Kg".format(menor, maior))