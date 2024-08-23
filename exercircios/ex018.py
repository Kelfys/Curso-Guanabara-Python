'''faça um programa que eia um angunlo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo'''

import math

angulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math
