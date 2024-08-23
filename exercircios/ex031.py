'''desenvolva um programa que pergunte a distanccia de uma viagem em km . calcule o preço da passagem cobrando r$ 0,50 por km para viagens de até 200km e r$ 0,45 para viagens mais longas.'''
distancia = float(input("digite a distanciada viagem em km :"))

if distancia <= 200:
    print(f"o preço da passagem e de {distancia * 0.50}")
else:
    print(f"o preço da passagem e de {distancia * 0.45}")

