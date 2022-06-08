#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
num=int(input("Digite um número: "))
parim=num%2
if parim==0:
    print("Esse número é PAR.")
else:
    print("Esse número é IMPAR.")