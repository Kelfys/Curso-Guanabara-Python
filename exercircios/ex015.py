'''escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.'''

km = float(input('quantos km rodados?'))
dias = int(input('quantos dias de aluguel?'))
preço = (km * 0.15) + (dias * 60)
print('o preço a pagar é de R${:.2f}'.format(preço))
