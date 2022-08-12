#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro), 
#e o programa irá informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print("="*50)
print("{:^50}".format("BANCO"))
print("="*50)
saque = int(input("Digite o valor que deseja sacar. R$:"))
notas50 = saque//50
saque = saque % 50
if notas50 !=0:
    print(f"\nSerão {notas50} notas de R$50.")
notas20 = saque//20
saque = saque % 20
if notas20 != 0:
    print(f"\nSerão {notas20} notas de R$20.")
notas10 = saque//10
saque = saque % 10
if notas10 != 0:
    print(f"\nSerão {notas10} notas de R$10.")
notas1 = saque // 1
saque = saque % 1
if notas1 != 0:
    print(f"\nSerão {notas1} notas de R$1.")
print("="*50)
print("Programa finalizado")