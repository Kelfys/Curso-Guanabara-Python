'''faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados'''

num = int(input('Digite um numero de 0 a 9999: '))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))
