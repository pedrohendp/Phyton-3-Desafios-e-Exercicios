#import math
from math import hypot
cateto1 = float(input('Comprimento do cateto oposto: '))
cateto2 = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)
hipotenusa = hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
