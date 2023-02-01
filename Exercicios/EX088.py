# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, mostrando tudo em uma lista composta.
import random, time

quant = int(input("Diga a quantidade de jogos a serem sorteados: "))
jogos = []
valores = []
for n in range(0,quant):
    cont = 0
    while cont < 6:
        num = random.randint(1,60)
        if num not in valores:
            valores.append(num)
            cont+=1
    valores.sort()
    jogos.append(valores[:])
    valores.clear()
print(f"Os {quant} jogos foram: ")
for i in range(0,quant):
    print(f"Jogo [{i+1}/{quant}] : {jogos[i]}")
    time.sleep(1)
