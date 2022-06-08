#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 ara viagens mais longas.
dist=int(input("A viagem que vc vai fazer é de quantos KM?\n"))
if dist>200:
    preço=float(dist*0.45)
else:
    preço=float(dist*0.50)
print("Você vai ter que pagar R${:.2f} pela passagem.".format(preço))