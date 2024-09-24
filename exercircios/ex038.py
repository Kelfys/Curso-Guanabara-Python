#escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor e maior
#o segundo valor e maior
#os dois valores sao iguais

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print('o primeiro valor e maior')
elif n2 > n1:
    print('o segundo valor e maior')
else:
    print('os dois valores sao iguais')