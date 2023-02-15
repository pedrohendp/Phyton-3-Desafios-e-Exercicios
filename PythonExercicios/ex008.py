distancia = float(input('Uma distância em metros :'))
km = distancia/1000
hm = distancia/100
dam = distancia/10
dm = distancia*10
cm = distancia*100
mm = distancia*1000
print('A medida de {:.1f} corresponde a'.format(distancia))
print('{:.3f}km'.format(km))
print('{:.2f}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}nm'.format(mm))
