dias = int(input('Quantos dias alugados ?'))
kmRodado = float(input('Quantos Km rodados ?'))
total = (dias * 60) + (kmRodado * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
