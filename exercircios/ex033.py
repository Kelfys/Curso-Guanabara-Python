'''faça um programa qye leia 3 nnumerose mostre qual e o maior e qual e o menor '''

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
n3 = int(input("digite o terceiro numero: "))
#verificando quem e o menor
if n1 < n2 and n1 <n3:
    print("esse e o menor numero: {}".format(n1))
if n2 < n1 and n2 < n3:
    print("esse e o menor numero: {}".format(n2))
if n3 < n1 and n3 < n2:
    print("esse e o menor numero: {}".format(n3))
