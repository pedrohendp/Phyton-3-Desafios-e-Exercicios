nome = str(input('Qual é o seu nome completo ?')).strip()
validar = 'SILVA' in nome.upper()
print('Seu nome tem Silva ? {}'.format(validar))
