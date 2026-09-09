#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario do funcionario:'))
aumento = salario + (salario * 15 /100)

print(f'O salario inicial de R${salario:.2f} com o aumento de 15% foi para R${aumento:.2f}')
