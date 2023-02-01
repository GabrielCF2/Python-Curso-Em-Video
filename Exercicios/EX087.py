# Aprimore o exercício anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

soma = som3 = som2l = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]] #isso daqui tá feio de mais
for i in range(0,3):
    for j in range(0,3):
        num = int(input("Digite um valor: "))
        matriz[i][j] = num
        if num%2==0:
            soma +=num
        if j == 2:
            som3 +=num
        if i == 1:
            if som2l<num:
                som2l = num
print("A matriz formatada é: ")
for k in range(0,3):
    print(matriz[k][:])
print(f"A soma dos valores é {soma}.")
print(f"A soma dos valores da terceira coluna é {som3}.")
print(f"O maior valor da segunda linha é {som2l}.")