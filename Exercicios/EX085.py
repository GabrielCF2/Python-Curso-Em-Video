# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# pares =[]
# impares = []
# lista = [pares, impares]
lista = [[],[]]
for n in range(0,7):
    num = int(input(f"Digite o valor [{n+1}/7]: "))
    if num%2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f"A lista com os valores pares e ímpares separados é {lista}")
lista[0].sort()
lista[1].sort()
print(f"A lista com os valores pares e ímpares separados e ordenados é {lista}")
ordenado = lista[0][:] + lista[1][:]
ordenado.sort()
print(f"Esses valores ordenados é {ordenado}")