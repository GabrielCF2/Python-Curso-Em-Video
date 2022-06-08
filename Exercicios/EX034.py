#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal=float(input("Digite o valor do salário: R$"))
if sal>1250:
    salnovo=sal+ (sal*0.10)
else:
    salnovo= sal+(sal*0.15)
print("Seu antigo salário era R${:.2f}. Seu novo salário é: {:.2f}".format(sal,salnovo))