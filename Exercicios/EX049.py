#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
n = int(input("Digite um número para ter a sua tabuada de 1 a 10: "))
for c in range(1,11):
    d = n*c
    print("{} X {} = {}".format(n,c,d))