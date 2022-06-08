#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez.
frase = str(input("Digite uma frase: ")).strip().lower()
print("Nessa frase a palavra 'a' aparece {} vezes.".format(frase.count("a")))
print("A primeira letra 'a' aparece na posição {}.".format(frase.find("a")+1))
print("A ultima letra 'a' aparece na posição {}.".format(frase.rfind("a")+1))