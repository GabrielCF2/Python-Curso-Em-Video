# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutua na tela.
aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['aprovado'] = 'Arpovado'
elif 5<= aluno['media'] <7:
    aluno['aprovado'] = 'Recuperação'
else:
    aluno['aprovado'] = 'Reprovado'
print('-='*30)
for k,v in aluno.items():
    print(f"{k} é igual a {v}")
# print(f"Nome é igual a {aluno['nome']} ")
# print(f"Média é igual à {aluno['media']}")
# print(f"E a sua situação é de {aluno['aprovado']}")
