# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura de sua parede: '))
altura = float(input ('Digite a altura de sua parede: '))
area = largura * altura

print(f'Sua parede tem a dimensao de {largura} x {altura}, e sua area eh de {area}m².\npara pintar essa parede, voce precisara de {area/2}L de tinta')