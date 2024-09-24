#escreva umprograma para aprovar o emprestimo bancario para a compra
#o programa vai perguntar o valor da casa, o salario do comprador e quantos anos ele vai pagar. calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

casa = float(input('qual o valor da casa? '))
salario = float(input('qual o seu salario? '))
anos = int(input('em quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
minimo = (salario * 30) / 100

print('para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação mensal vai ser de R${:.2f}'.format(prestacao))

print("fim ddo programa")