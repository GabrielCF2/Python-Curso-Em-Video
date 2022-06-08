#Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, 
#o salário do comprador e em quantos anos ele vai pagar.
print("Programa para calcular empréstimo de financiamento de uma casa.")
casa = float(input("Digite o valor da casa que vai financiar: R$"))
salario = float(input("Digite o valor do seu salário mensal: R$"))
ano = int(input("Digite a quantidade de anos que pretentde pagar esse empréstimo: "))
presmes = (casa/ano)/12
if presmes > (salario*0.3):
    print("Desculpe mas as prestações excedem 30% do seu salário")
else:
    print("Com o seu salário de R${}. A sua casa no valor de R${} será paga em {} anos em prestações de R${}.".format(salario,casa, ano,presmes))