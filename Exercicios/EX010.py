#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar
r=float(input("Digite quantos reais você tem na carteira: R$"))
d=r/5.55 #Cotação 12/01/2022
print("Com R${:.2f} você pode comprar US${:.2f}".format(r,d))