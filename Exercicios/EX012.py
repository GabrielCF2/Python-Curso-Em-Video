#Faça um algoritmo que leia o preço de um produto e forneça seu novo preço com 5% de desconto
v=float(input("Digite o preço de um produto: R$"))
d=v-(v*0.05)
print("O produto custa R${}".format(v))
print("Esse produto com 5% desconto fica R${:.2f}".format(d))