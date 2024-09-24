#eescreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão: 1 para binario, 2 para octal e 3 para hexadecimal

num = int(input('digite um numero: '))
print('''escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('sua opção: '))
if op == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{}, convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida, tente novamente')