#Faça um programa que joque par ou impar com o cumputador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
cont = 0
while True:
    n = int(input("Escolha um número: "))
    escolha = str(input("Escolha entre Par e Impar. [P/I]: ")).upper()
    while escolha != 'P' and escolha != 'I':
        escolha = str(input("Escolha Par ou Impar. [P/I]: ")).upper()
    oponente = randint(0,10)
    total = oponente + n
    print(f"Você escolheu {n} e o computador escolheu {oponente}, o resultado foi {total}", end=' ')
    if (total % 2) == 0:
        print("que é Par.")
        if escolha == 'P':
            print("Você ganhou!!")
            cont +=1
        else:
            print(f"Você perdeu!\nVocê ganhou {cont} vezes seguidas.")
            break
    else:
        print("que é Impar.")
        if escolha == 'I':
            print("Você ganhou!!")
            cont +=1
        else:
            print(f"Você perdeu!\nVocê ganhou {cont} vezes seguidas.")
            break
print("JOGO FINALIZADO!!")