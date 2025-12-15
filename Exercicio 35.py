import math

print('Olá precisamos de algumas informações para informar o aumento!')
salario = float(input('Digite o valor do salário do funcionário:R$'))
if salario > 1250.00:
    aumento = salario + (salario*0.10)
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')
else:
    salario <= 1250.00
    aumento = salario + (salario*0.15)
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')