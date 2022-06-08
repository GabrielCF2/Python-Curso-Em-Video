#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
dias=int(input("Escreva a quantidade de dias que o carro foi alugado: "))
km=float(input("Escreva a quantidade de Km que esse carro percorreu: "))
valor=(km*0.15)+(dias*60)
print("O carro foi alugado por {} dias e que percorreu {}Km".format(dias, km))
print("Você terá que pagar um total de RS{:.2f}".format(valor))