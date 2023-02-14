# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira funão vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma trodos os valores PARES sorteados pela função anterior.
from random import choice
def somaPar(lista):
    print(f"A lista de valores sorteados foi: {lista}")
    soma = 0
    for n in lista:
        if n%2==0:
            soma+=n
    print(f"A soma dos valores pares é {soma}.")
def sorteia(lista):
    print(f"A lista dos valores a serem sorteados é: {lista}")
    sort = []
    for n in range(5):
        sort.append(choice(lista))
    somaPar(sort)
numeros = [2,1,5,7,6,3,8,12,4,8,13,16,15]
sorteia(numeros)