#Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, 
#com uma pausa de um segundo entre eles.
from time import sleep
print("A contagem de fogos irá começar!")
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print("Que comecem os fogos.")
print("BOOM POW KABUM")