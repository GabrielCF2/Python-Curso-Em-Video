# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de cada jogador.
jogador = {}
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    jogador['partidas'] = int(input("Qantas partidas ele jogou: "))
    jogador['gols'] = []
    jogador['aproveitamento']=0
    for p in range(0,jogador['partidas']):
        gols = int(input(f"Quantos gols {jogador['nome']} fez no {p+1}º jogo [{p+1}/{jogador['partidas']}]: "))
        jogador['aproveitamento']+= gols
        jogador['gols'].append(gols)
    time.append(jogador.copy())
    # jogador['gols'].clear()
    # con = str(input("Quer continuar? [S/N]: "))
    # if con in 'nN':
    #     break
    while True:
        resp = str(input("Quer continuar: [S/N]: ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas com  S ou N.")
    if resp == 'N':
        break
print('-='*30)
print(f"cod ", end='')
for i in jogador.keys():
    print(f"{i:<15}",end='')
print()
print('-='*30)
for n,j in enumerate(time):
    print(f"{n:<3}",end='')
    for d in j.values():
        print(f"{str(d):<15}", end='')
    print()
num = 0
print("-="*30)
while num>=0:
    num = int(input("Quer mostrar o levantamento de qual jogador? (Numero negativo para parar): "))
    if num >= len(time):
        print(f"Erro! Não exite jogador com código {num}")
    else:
        print('--'*30)
        print(f"Levantamento do jogador {time[num]['nome']}")
        for j,g in enumerate(time[num]['gols']):
            print(f"No jogo {j+1} fez {g} gols.")
        print('--'*30)
print("<<<VOLTE SEMPRE>>>")


# print('-='*30)
# print(jogador)
# print('-='*30)
# for k, v in jogador.items():
#     print(f"O campo {k} tem o valor {v}")
# print('-='*30)
# print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
# for p,g in enumerate(jogador['gols']):
#     print(f"=>Na partida {p+1}, fez {g} gols.")
# print(f"Foi um total de {jogador['aproveitamento']} gols.")
# print('-='*30)
