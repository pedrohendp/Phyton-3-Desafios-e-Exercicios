valor = float(input('Qual é o preço do produto? R$'))
desconto = valor * 0.05
#OU ENTÃO -> valorDesconto = valor - (valor * 5/100)
valorDesconto = valor - desconto
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(valor, valorDesconto))
