#Melhore o desafio 61, perguntando para o usuário se ele quer digitar mais alguns termos.
#o programa acaba quando ele disser que quer mostrar 0 termos.
print("Vamos calcular a PA de um número.")
n = int(input("Escolha o primeiro número da PA: "))
r = int(input("Agora escolha a razão da PA: "))
cont = 0
val = 10
print("Os 10 primeiros termos da PA são: ")
while cont<val:
    cont=cont+1
    print(n, end=' ')
    n +=r
    if cont==val:
        print("\nDeseja mostrar mais números?")
        val += int(input("Digite quantos mais números vc quer que sejam mostrados: "))
print("Programa finalizado!")