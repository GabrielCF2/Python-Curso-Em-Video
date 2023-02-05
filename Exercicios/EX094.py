# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# C) Um lista com todas as pessoas com idade a cima da média.
pessoa = {}
pessoas = []
while True:
    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo: [M/F] ").upper())
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input("Sexo: [M/F] ").upper())
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    con = str(input("Deseja continuar? [S/N]: "))
    if con in 'nN':
        break
media = 0
mulheres = []
dot = []
for i in pessoas:
    media += i['idade']
    if i['sexo'] in 'F':
        mulheres.append(i)
media = media//len(pessoas)
for i in pessoas:
    if i['idade']>media:
        dot.append(i)
print('-='*30)
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"A idade média do grupo é de {media}")
print(f"As mulheres do grupo são: {mulheres}")
print(f"Quem tem a idade a cima da média é {dot}")
