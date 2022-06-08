#Faça um programa que leia a altura de uma parede em metros, calcule a sua áre e a quantidade de tinha necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
larg=float(input("Largura da parede: "))
alt=float(input("Altura da parede: "))
area=larg*alt
tinta=area/2
print("A parede com {:.2f}metros de largura e {:.2f}metros de altura tem uma área de {:.2f}metros quadrados".format(larg,alt,area))
print("E precisará de {:.2f}litros de tinha para ser pintada.".format(tinta))