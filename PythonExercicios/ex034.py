salario = float(input('Qual é o salário do funcionário ? '))
if salario >= 1250:
    reajuste = salario + (salario * 10 / 100)
else:
    reajuste = salario + (salario * 15 / 100)
print('Quem ganhava R${:.2f} passou a ganhar R${:.2f} agora '.format(salario, reajuste))
