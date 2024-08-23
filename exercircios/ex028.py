'escreva um ´rograma que faça o computador pensar em um numero inteiro emtre 0 e 5 e faça para o usuario tentar descobrir qqual foi o numero escolhido pelo computador.  o programa debvera escrever na o usuario venceu ou perdeu'

from random import randint

num = int(input("digite um numero de 1 a 5: "))
num_user = randint(1, 5)
while num_user != num:
    print("voce perdeu")
    num = int(input("digite um numero de 1 a 5: "))
    num_user = randint(1, 5)
if num_user == num:
    print("voce venceu")

