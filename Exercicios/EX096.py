# Crie um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(x,y):
    a = x*y
    print(f"A área do terreno de {x}x{y} é de {a:.1f}m².")

print('Controle de terreno\n','-='*20)
x = float(input('Largura (m): '))
y = float(input('Comprimento (m): '))
area(x,y)