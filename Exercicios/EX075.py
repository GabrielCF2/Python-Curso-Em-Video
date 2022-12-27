# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No fial mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os valores pares.
# VER COMO QUE FAZ
from random import randint

numero = [0,0,0,0]
for i in range(0,4):
    numero[i] = int(input("Digite um valor: "))
tupla = tuple(numero)
print(tupla)
n9 = tupla.count(9)
print(f"O valor 9 apareceu {n9} vezes")
if 3 in numero:
    print(f"O numero 3 apareceu primeiro na {tupla.index(3) +1}ª posição.")
else:
    print("O número 3 não apareceu")
print("Os valores pares digitados foram ", end='')
for n in numero:
    if n % 2 == 0:
        print(n,end=' ')