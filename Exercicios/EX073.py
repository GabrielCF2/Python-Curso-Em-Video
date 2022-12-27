# Crie um a tupla com os 20 primeiros colocados do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados
# C) uma lista com os times em ordem alfabética
# Em que posição está o time da Chapecoense (Não tava na lista então escolhi Flamengo).

tabela = ('Palmeiras', 'Internacional', 'Fluminense', "Corinthians",'Flamengo', 'Athletico-PR', 'Atltético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
print("-="*15)
print(f"A lista de times é {tabela}")
print("-="*15)
print(f'Os 5 primeiros ítens da tabela são {tabela[0:5]}')
print("-="*15)
print(f'Os 4 últimos ítens da tabela são {tabela[16:20]}')
print("-="*15)
tupla_ordenada = sorted(tabela)
print(f"A tupla ordenada em ordem alfabética é {tupla_ordenada}")
print("-="*15)
flamengo = tabela.index('Flamengo')+1
print(f" O time Flamengo está na {flamengo}ª posição ")
print("-="*15)
