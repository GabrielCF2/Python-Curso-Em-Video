# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados de forma tabular.
tupla = ('lapis', 1.75, 'borracha', 2, 'caderno', 25.90, 'estojo', 25, 'transferidor',4.20, 'compasso', 9.99, 'mochila', 120, 'canetas', 21.20, 'livro', 34.9)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}',end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')
print('-'*40)
