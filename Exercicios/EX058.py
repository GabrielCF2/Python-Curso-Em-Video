#Melhore o jogo do desafio 28 onde o computador vai "pensar" num número entre 0 e 10.
# Só qur agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint


palpites = 0
print("O computador vai escolher um número entre 0 e 10, tente adivinhar qual é.")
participante = int(input("Digite um número ente 0 e 10: "))
computador = randint(0,10)
while participante != computador:
    participante = int(input("Você errou o número, tente novamente: "))
    palpites += 1
print(f"Você acertou, o número era {computador}, precisou de apenas {palpites} tentativas para acertar.")