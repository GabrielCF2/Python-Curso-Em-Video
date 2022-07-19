#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = 0
menor = int(input("Digite um valor: "))
continuar = 's'
cont=0
total=0
while continuar!='N':

    continuar =input("Deseja continuar? Digite [S] para continuar e [N] para prarar: ").upper()
    if continuar == 'S':
        cont+=1
        num = int(input("Digite um número: "))
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        total += num
media = total/cont
print(f"A média dos valores é {media}, o maior número digitado foi {maior} e o menor número digitado foi {menor}.")
