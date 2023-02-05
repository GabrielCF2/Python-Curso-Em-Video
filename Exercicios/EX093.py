# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois ele vai perguntar a quantidade de gols feita em cada partida. No final, tudo isso será guardado em um dicionár, incluindo o total de gols feitos durante o campeonato.
jogador = {}
jogador['nome'] = str(input("Digite o nome do jogador: "))
tot = int(input("Qantas partidas ele jogou: "))
jogador['gols'] = []
jogador['total']=0
for p in range(0,tot):
    gols = int(input(f"Quantos gols {jogador['nome']} fez no {p+1}º jogo [{p+1}/{tot}]: "))
    jogador['total']+= gols
    jogador['gols'].append(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*30)
print(f"O jogador {jogador['nome']} jogou {tot} partidas.")
for p,g in enumerate(jogador['gols']):
    print(f"    => Na partida {p+1}, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols.")
print('-='*30)
