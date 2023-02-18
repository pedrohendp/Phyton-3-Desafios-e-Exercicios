import math
valor = float(input('Digite um valor:'))
inteiro = math.floor(valor)
print('O valor digitado foi {} e sua porção inteira é {}'.format(valor, inteiro))
print('O valor digitado foi {} e sua porção inteira é {}'.format(valor, math.trunc(valor)))
 