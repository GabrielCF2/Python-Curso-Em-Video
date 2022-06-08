# esse programa vai calcular o dobro, o triplo, e raiz quadrada.
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = pow(n, (1/2))
print("O dobro de {} é {}.".format(n, d))
print("O triplo de {} é {}.".format(n, t))
print("A raiz quadrada de {} é {:.3f}.".format(n, r))
