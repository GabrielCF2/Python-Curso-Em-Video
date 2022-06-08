#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

pagamento = int(input("Digite o valor do pagamento: R$"))
formapag = int(input('''Informe o tipo de pagamento:
[1] Pagamento à vista no dinheiro ou cheque
[2] Pagamento à vista no cartão
[3] Pagamento parcelado em até 2x no cartão
[4] Pagamento parcelado em 3x ou mais no cartão
'''))
if formapag == 1:
    total = pagamento - (pagamento * 0.1)
elif formapag == 2:
    total = pagamento - (pagamento * 0.05)
elif formapag == 3:
    total = pagamento
    parcela = pagamento / 2
    print("Sua compra será parcelada em 2x de R${:.2f}.".format(parcela))
elif formapag == 4:
    total = pagamento + (pagamento * 0.2)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}x de R${:.2f}. COM JUROS".format(totparc,parcela))
else:
    total = pagamento
    print("Forma de pagamento inválida.")
print("Você escolheu a opção [{}]. A compra de R${:.2f} irá sair a : R${:.2f}".format(formapag, pagamento,total))