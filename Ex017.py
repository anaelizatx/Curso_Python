# Faça um programa que leia o comprimento do 
# cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Digite o cateto oposto de um triângulo retângulo: '))
adjacente = float(input('Digite o cateto adjacente de um triângulo retângulo: '))

hipotenusa = hypot(oposto , adjacente)

print (f'O valor da hipotenusa eh: {hipotenusa}')
