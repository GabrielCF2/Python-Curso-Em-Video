# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é o maior.
def maior(*num):
    print('=='*20)
    print("Analizando os valores passados...")
    mai = 0
    for n in num:
        if n>mai:
            mai = n
        print(n,end=' ')
    print(f"Foram analizados {len(num)} valores ao todo.")
    print(f"O maior valor é {mai}.")
    print('=='*20)


maior(2,5,4,6,9)