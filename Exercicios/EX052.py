#Faça um programa que leia um número e diga se ele é ou não um número primo.

#não sei como resolver
n=int(input("Digite um número: "))
cont=0
for c in range(1,n+1):
    if (n%c) == 0:
        #print("\033[33m",end='')
        cont+=1
    #else:
        #print("\033[31m",end='')
    #print(c,end=' ')
#print("\033[mO número {} foi dividido {} vezes.".format(n,cont))
if cont == 2:
    print("O número {} é primo.".format(n))
else:
    print("O número {} NÃO é primo.".format(n))