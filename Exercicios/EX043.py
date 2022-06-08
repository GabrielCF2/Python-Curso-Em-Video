#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
altura = (int(input("Diga a sua altura em cm: ")))/100
peso = float(input("Diga o se peso em Kg: "))
media = peso / (altura**2)
print("O imc dessa pessoa é {:2f}".format(media))
if media <18.5:
    print("Abaixo do Peso.")
elif media < 25:
    print("Peso ideal.")
elif media < 30:
    print("Sobrepeso.")
elif media < 40:
    print("Obesidade.")
else:
    print("Obesidade Mórbida")
