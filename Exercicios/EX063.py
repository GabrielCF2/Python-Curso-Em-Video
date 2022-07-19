#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
cont = 0
fib0 = 0
fib1 =1

n = int(input("Digite a quantidade de elementos da sequência de fibonacci que vc quer que seja mostrada: "))
print(f"Os {n} primeiros termos da sequência são: ")
while cont<n:
    print(fib0,end=', ')
    aux = fib1
    fib1 +=fib0
    fib0=aux
    
    cont +=1
print("\nAcabou!")