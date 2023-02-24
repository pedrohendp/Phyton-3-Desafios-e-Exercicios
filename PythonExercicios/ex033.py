val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor: '))
val3 = int(input('Terceiro valor: '))
#Verificando o menor
menor = val1
if val2 < val1 and val2 < val3:
    menor = val2
if val3 < val1 and val3 < val2:
    menor = val3
#Verificando o maior
maior = val1
if val2 > val1 and val2 > val3:
    maior = val2
if val3 > val1 and val3 > val2:
    maior = val3
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
