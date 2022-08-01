#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido se o valor solicitado for negativo.
print("Esse programa vai mostrar a tabuada de 1 a 10 do número escolhido.")
while True:
    print("=-"*30)
    n = int(input("Digite um número para saber a sua tabuada: "))
    if n < 0:
        break
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
print("PROGRAMA FINALIZADO!!")