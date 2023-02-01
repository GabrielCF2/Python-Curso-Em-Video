# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em um alista. No final, moste:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoa = []
dados = []
pesado = leve = cont = 0
while True:
    cont +=1
    dados.append(str(input("Digite o nome: ")))
    dados.append(int(input("Digite o peso: ")))
    pessoa.append(dados[:])
    if cont == 1:
        pesado = dados[1]
        leve = dados[1]
    elif dados[1]>pesado:
        pesado = dados[1]
    elif dados[1]<leve:
        leve = dados[1]
    dados.clear()
    c = str(input('Quer continuar? [S/N] '))
    if c in 'nN':
        break
print(f"Foram inseridas {cont} pessoas.")
print(f"O maior peso foi de {pesado} e as pessoas com esse peso foram: ",end='')
for p in pessoa:
    if p[1]==pesado:
        print(f"{p[0]}, ",end='')
print(f"\nO menor peso foi de {leve} e as pessoas com esse peso foram: ",end=' ')
for p in pessoa:
    if p[1]==leve:
        print(f"{p[0]}, ",end='')