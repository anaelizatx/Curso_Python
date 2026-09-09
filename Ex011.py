# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor do produto: '))
desconto = valor * 5 / 100

print(f'O valor final com 5% de desconto sera de R$:{valor - desconto:.2f}')    