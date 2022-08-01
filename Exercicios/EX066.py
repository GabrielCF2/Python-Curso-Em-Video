#Crie um programa que leia vários números inteiros pelo teclado.
#o programa só vai parar quando o usuário digitar o número 999, que é a condição de parada.
#No final mostre quantos números foram digitados e qual foi a soma entre eles desconsiderando a flag.
n  = soma = 0
cont = -1

while True:
    if n==999:
        break    
    soma +=n
    n = int(input("Digite um número: "))
    
    cont+=1

print(f"Foram digitados {cont} números, e a soma deles foi {soma}.")