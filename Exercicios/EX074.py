# Crie um programa que gere 5 números alatórios e coloque em um atupla.
# Depois disso, mostre a listagem de números gerados e também o menos e o maior valor que estão na tupla.
from random import randint
tupla = tuple(randint(1,10) for i in range(0,5))
print(f"Os números gerados foram: {tupla}")
print(f"O menor valor foi {min(tupla)}")
print(f"O maior valor foi {max(tupla)}")
