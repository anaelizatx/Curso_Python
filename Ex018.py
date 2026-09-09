# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

angulo = int(input('Digite o angulo: '))

print(f'O seno deste angulo eh {sin(radians(angulo))}, o cosseno eh {cos(radians(angulo))} e a tangente eh {tan(radians(angulo))}')