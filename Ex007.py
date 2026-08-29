# Escreva um programa que leia um valor 
# em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
print(f'{medida} metros eh equivalente a {cm} centimetros e {mm} milimetros')