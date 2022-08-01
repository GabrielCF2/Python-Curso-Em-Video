#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deve perguntar se o usuário quer continuas ou não.
#No final deve mostrar:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.
mais18 = homens = mulheres20= 0
while True:
    print('-'*30)
    print("Digite a didade e o sexo de uma pessoa.")
    idade = int(input("Digite a idade da pessoa: "))
    print('-'*30)
    sexo = str(input("Digite o sexo da pessoa. [M/F]: ").upper())
    print('-'*30)
    if 'M' != sexo != 'F':
        sexo = str(input("Digite o sexo da pessoa. [M/F]:").upper())
        print('-'*30)
    if idade > 18:
        mais18 +=1
    if sexo == 'M':
        homens +=1
    elif idade < 20:
        mulheres20 +=1
    parar = str(input("Deseja continuar? [S/N]: ").upper())
    print('-'*30)
    if "S" != parar != "N":
        parar = str(input("Deseja continuar? [S/N]: ").upper())
        print('-'*30)
    if parar == 'N':
        break
    

print(f"Foram cadastradas {mais18} pessoas com mais de 18 anos, {homens} homens e {mulheres20} mulherses com menos de 20 anos.")