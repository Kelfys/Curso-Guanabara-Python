'''faça um programa que leia o nome competo de uma pessoa e mostre o primeiro e o ultimo nome separadamente'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu ultimo nome é {}'.format(nome.split()[-1]))
