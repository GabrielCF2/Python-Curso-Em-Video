#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal=float(input("Digite o salário do funcionário: R$"))
aum=sal+(sal*0.15)
print("O salário que antes era de R${:.2f} agora é de R${:.2f}".format(sal,aum))