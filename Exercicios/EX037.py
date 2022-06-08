#Escreva um programa que leia um número qualquer e peça ao usuário para escolher qual a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal
num = int(input("Digite um número: "))
n=int(input("Escolha para qual base ele será convertido: \n1 = binário, \n2 = octal, \n3 = hexadecimal\n"))
if n == 1:
    print("O número {} em binário é {}".format(num,bin(num)[2:]))
elif n == 2:
    print("O número {} em octal é {}".format(num, oct(num)[2:]))
elif n == 3:
    print("O número {} em hexadecimal é {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida!")