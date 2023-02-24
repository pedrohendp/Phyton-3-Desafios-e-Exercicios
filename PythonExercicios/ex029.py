velocidade = int(input('Qual é a velocidade do carro ?'))
velocidadePermitida = 80
multa = (velocidade - velocidadePermitida) * 7
if velocidade > velocidadePermitida:
    print('MULTADO! Você exedeu o limite permitido é de {}Km/h, você foi multado em {}'.format(velocidadePermitida, multa))
else:
    print('Tenha um bom dia! Dirija com segurança')
