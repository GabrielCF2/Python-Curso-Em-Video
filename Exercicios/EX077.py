# Crie um programa que tenha uma tupla com várias palavras (não usando acentos). Depois disso, você deve mostras, para cada palavra, quais são as suas vogais.
palavras = ('farinha', 'batata', 'arroz', 'manjericão', 'condimento', 'bermuda', 'fome')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
