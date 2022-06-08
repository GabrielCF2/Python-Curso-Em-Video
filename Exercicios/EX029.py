#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa deve custar R$7,00 por cada Km acima do limite.

v_max=80.00
vel=float(input("O carro estava a quantos Km/h? : "))
if vel>v_max:
    v=(vel-v_max)
    v=v*7
    print("Você ultrapassou o limte de velocidade de 80Km/h.")
    print("Você estava dirigindo a {:.0f}Km/h.".format(vel))
    print("Vai ter que pagar uma multa de R${:.2f}.".format(v))
else:
    print("\nVocê não ultrapassou o limite de velocidade.")
    print("Muito bem!")
print("Tenha um bom dia. Dirija com segurança.")