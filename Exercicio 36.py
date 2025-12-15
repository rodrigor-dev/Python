'''Desenvolva um programa que leia o comprimento de três retas a diga ao usuário se elas podem ou não formar um triângulo.'''

print('-=-' * 35)
print('Por favor, informe os comprimentos de três retas para dizer se elas podem ou não formar um triângulo')
print('-=-' * 35)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('Os valores acima PODEM FORMAR um triângulo!')
else:
    print('Os valores acima NÃO PODEM FORMAR um triângulo!')