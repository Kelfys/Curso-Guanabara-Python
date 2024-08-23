'''escreva um programa que leia a velocidade do carro, se eel ukltrapasssar 80km/h.mostre uma mensagem dizendo que ele foi multado a multa vai custarrs 7.00 por cada km acima do limite'''

velocidade = int(input("digite a sua velocidade: "))
if velocidade > 80:
    print("Você foi multado!")
    print(f"sua multa foi de R${(velocidade - 80) * 7}")
else:
    print("vc nao foi multado")
