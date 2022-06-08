# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros.
m = float(input("Digite um valor em metros: "))
cm = m * 100
mm = m * 1000
print("Esse valor é igual a {}cm e {}mm".format(cm, mm))
