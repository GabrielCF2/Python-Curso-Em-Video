# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
index = -1
while(not(0<=index<=20)):
    index = int(input('Digite um número entre (0 e 20): '))
print(f"O número que você digitou fica {numeros[index]} por extenso.")