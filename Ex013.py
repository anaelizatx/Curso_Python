#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = int(input('Digite a temperatura em °C: '))
fahrenheit = celsius * 1.8 + 32

print(f'A temperatura de {celsius}°C corresponde a {fahrenheit:.0f}°F ')