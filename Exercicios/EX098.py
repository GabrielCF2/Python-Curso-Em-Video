# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e paso e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada.
# A) De 1 até 10 de 1 em 1
# B) De 10 até 0 de 2 em 2
# C) Uma contagem personalizada.
from time import sleep
def contagem(inicio, fim, passo):
    if passo<0:
        passo *=-1
    if passo==0:
        passo = 1
    print(f"Iniciando contagem de {inicio} até {fim} de {passo} em {passo}.")
    if inicio>fim:
        fim = fim-1
        passo = passo*-1
    else:
        fim +=1

    print(f"-="*25)
    for n in range(inicio, fim, passo):
        print(f'{n}',end=' ',flush=True)
        # sleep(0.5)
    print("FIM!")
    print()


contagem(1,10,1)
contagem(10,0,2)
print("Agora é a sua vez de personalizar a contagem.")
inicio = int(input('INICIO: '))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))
contagem(inicio, fim, passo)
