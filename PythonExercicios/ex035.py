print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else :
    print('Os segmentos acima NAO PODEM FORMAR um triângulo')
