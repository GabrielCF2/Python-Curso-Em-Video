# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(frase):
    tam = len(frase)+4
    print('~'*tam)
    print(f"{frase:^{tam}}")
    print('~'*tam)
    

pal = str(input('Digite uma frase qualquer: '))
escreva(pal)
# escreva('era uma vez um mundo vazio')