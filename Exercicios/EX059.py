#Crie um programa que leia dois valores e mostre um menú na tela:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS 
#[5] SAIR DO PROGRAMA
#Seu programa deverá realizar a operação solicitada em cada caso.
print("Digite dois valores e depois escolha as opções.")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
escolha = 0
while escolha != 5:
    escolha = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS 
[5] SAIR DO PROGRAMA
Escolha uma das opções acima: '''))
    if escolha <=0 or escolha>5:
        print("Você digitou um valor inválido, tente novamente.")
    elif escolha == 1:
        print(f"A soma de {num1} + {num2} = {num1+num2}.")
    elif escolha == 2:
        print(f"O produto de {num1} X {num2} = {num1*num2}.")
    elif escolha == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num2 > num1:
            print(f"{num2} é maior que {num1}")
        elif num1 == num2:
            print(f"Os dois valores são iguais. O valor é {num2}.")
        else:
            print("Se isso apareceu então algo deve estar errado.")
    elif escolha == 4:
        print("Digite novos súmeros.")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    elif(escolha == 5):
        print("Bom, você escolheu fechar o programa.")
print("PROGRAMA FINALIZADO.")