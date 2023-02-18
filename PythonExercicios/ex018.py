from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja :'))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(angulo, tang))
