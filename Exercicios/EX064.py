#Crie um programa que leia vários números inteiros no teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
#No final mostre quantos números foram somados e qual foi a soma deles (desconsiderando a flag)
cont = -1
val = 0
n = 0
print("Digite vários números, para sair digire 999.")
while n != 999:
    val+=n
    cont +=1
    n = int(input("Digite um número: "))
print(f"Você digitou {cont} números e a soma deles deu {val}.")