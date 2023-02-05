# Ceie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Para se aposentar é 35 anos de contribuição.
import time

pessoa = {}
pessoa['nome'] = str(input("Nome: "))
pessoa['idade'] = (time.localtime()).tm_year - int(input('Ano de nascimento: ')) 
pessoa['CTPS'] = int(input("Carteira de trabalho (0 não tem): "))
if pessoa['CTPS'] != 0:
    pessoa['contrato'] = int(input("Ano de contratação: "))
    pessoa['salario'] = int(input("Salário: R$"))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (time.localtime().tm_year - pessoa['contrato']))
print('-='*30)
for k,v in pessoa.items():
    print(f"{k} tem o valor {v}")
# print(f"Nome tem o valor {pessoa['nome']}")
# print(f"Idade tem o valor {pessoa['idade']}")
# print(f"CTPS tem o valor {pessoa['CTPS']}")
# if pessoa['CTPS'] != 0:
#     print(f"Contratação tem o valor {pessoa['contrato']}")
#     print(f"Salário tem o valor {pessoa['salario']}")
#     print(f"Aposentadoria tem o valor {pessoa['aposentadoria']}")
