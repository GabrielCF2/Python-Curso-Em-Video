#Desenvolva um programa que leia o primeiro termo e a razão de uma pa.
#No final, mostre os 10 primeiros termos dessa progressão.

print("Vamos calcular uma Progressão Aritimética.")
p=int(input("Digite o primeiro termo: "))

r=int(input("Digite a razão: "))
print("Os 10 primeiros termos dessa PA são: ")
for c in range(0,10):
    print(p,end=' ')
    p+=r