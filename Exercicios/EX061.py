# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da prgreção usando a estrutura while.
print("Vamos calcular a PA de um número.")
n = int(input("Escolha o primeiro número da PA: "))
r = int(input("Agora escolha a razão da PA: "))
cont = 0
print("Os 10 primeiros termos da PA são: ")
while cont<10:
    cont=cont+1
    print(n, end=',')
    n +=r
