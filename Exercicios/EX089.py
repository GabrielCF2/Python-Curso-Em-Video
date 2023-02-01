# Crie um programa que leia nome e duas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# nome = str()
# notas = []
# lista = []
# cont=0

# while True:
#     cont+=1
#     nome = (str(input("Digite o nome do aluno: ")))
#     notas.append(float(input("Digite a primeira nota do aluno: ")))
#     notas.append(float(input("Digite a segunda nota do aluno: ")))
#     notas.append((notas[0]+notas[1])/2)
#     lista.append(nome)
#     lista.append(notas[:])
#     notas.clear()
#     # print(lista)
#     c = str(input("Deseja continuar? [S/N] "))
#     if c in 'nN':
#         break
# print(f"As notas dos alunos são: ")
# for a in range(0,cont):
#     print(f"{lista[a][0]}")

# while True:
#     num = int(input("Deseja ver a nota de qual aluno? (Digite um número negativo para parar.)"))
#     print(f"As notas de {lista[num][0]} são {lista[num][1]}")
#     if num <0:
#         break

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2 ) /2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "nN":
        break
print("-="*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-'*26)
for i,a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-"*35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <=len(ficha)-1:
        print(f"\nNotas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<<VOLTE SEMPRE>>>")