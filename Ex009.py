# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Digite quantos R$ voce tem na carteira:'))
dolar = reais / 5.10

print(f'Seu saldo em dolar eh de U${dolar:.2f}')
