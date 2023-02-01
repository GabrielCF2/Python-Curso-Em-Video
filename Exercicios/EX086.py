# Crie um programa que crie um a matriz 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação correta

matriz = [[],[],[]] #isso daqui tá feio de mais
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input("Digite um valor: ")))
print("A matriz formatada é: ")
for k in range(0,3):
    print(matriz[k][:])