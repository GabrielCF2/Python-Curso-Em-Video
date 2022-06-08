# Crie um programa que faça o computador jogar Jokenpô com você.
import random
escolhas = ["Pedra","Papel","Tesoura"]
print('''Vamos jogar pedra papel tesoura contra o computador.
''')
jogador = int(input('''Escolha a sua opção:
[1] Pedra
[2] Papel
[3] Tesoura
'''))
oponente = random.choice([1,2,3])
if (jogador == 1 and oponente == 2) or (jogador == 2 and oponente == 3) or (jogador == 3 and oponente == 1):
    print("\033[0;31mVocê perdeu, você escolheu {} e o computador escolheu {}\033[m".format(escolhas[jogador-1],escolhas[oponente-1]))
elif (jogador == 1 and oponente == 3) or (jogador == 2 and oponente == 1) or (jogador == 3 and oponente == 2):
    print("\033[0;32mVocê ganhou, você escolheu {} e o computador escolheu {}\033[m".format(escolhas[jogador-1],escolhas[oponente-1]))
elif jogador == oponente:
    print("Deu empate, ambos escolheram {}".format(escolhas[jogador-1]))
else:
    print("Você não escolheu entre as opções, tente novamente.")