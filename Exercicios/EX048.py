#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três 
# e se encontram no intervalo de 1 até 500.
acum = 0
cont = 0
for c in range(1,500,2):
    if(c%3==0):
        cont += 1
        acum += c
print("A soma dos {} números é {}.".format(cont,acum))