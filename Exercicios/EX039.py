#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
atual = datetime.date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar imediatamente.")
elif idade<18:
    ano = nasc + 18
    print("Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento.".format(18-idade))
    print("Seu alistamento será em {}.".format(ano))
elif idade > 18:
    ano = nasc + 18
    print("Você já deveria ter se alistado a {} anos.".format(idade - 18))
    print("Seu alistamento foi em {}.".format(ano))
