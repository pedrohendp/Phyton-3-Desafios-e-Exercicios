from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador Pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS!, você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
