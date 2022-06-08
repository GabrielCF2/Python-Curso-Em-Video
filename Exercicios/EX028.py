#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário 
#tentar descobrir qual foi o número escolhido pelo computador.
#O programa deve escrever na tela se o usuário venceu ou perdeu.
import random
n=random.randint(0,5)
print("Tente adivinhar que número o computador escolheu.")
u=int(input("Escolha um número entre 0 e 5.\n"))
if n==u:
    print("Parabéns, você acertou. O número era {}.".format(u))
else:
    print("Que pena, você errou. Você escolheu {} e o número era {}.".format(u,n))
