#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deve perguntar se o usuário vai continuar.
#No final mostre:
#A) Qual o total gasto na compra.
#B) Quantos produtos custam mais de R$100,00
#C) Qual o nome do produto mais barato.
cont =tot= 0
barato = 999999999999

while True:
    continuar = 'k'
    print('__'*20)
    print("Digite o nome e o preço de um produto.")
    nome = str(input("Digite o nome do produto: "))
    print('__'*20)
    preço = float(input("Digite o preço do produto: R$"))
    print('__'*20)
    tot +=preço
    if preço > 1000:
        cont+=1
    if preço < barato:
        barato = preço
        prodbarato = nome
    while 'S' != continuar != 'N':
        print('__'*20)
        continuar = str(input("Deseja continuar? [S/N]: ").upper())
    if continuar == 'N':
        break
print(f"O valor total da compra foi de R${tot}, {cont} produtos custaram mais de 100 reais, o produto mais varato foi {prodbarato}, custando R${barato}.")
