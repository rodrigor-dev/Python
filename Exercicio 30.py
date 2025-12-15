'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h. mostre uma mensagem dizendo que ele foi multado.
A multa vai custar
R$7.00 por cada Km acima do limite.'''

print('Limite da via 80 Km/h')
velocidade = int(input('Digite a velocidade atual do carro em Km/h: '))
if velocidade <=80: 
    print('Você está dentro do limite de velocidade.Tenha um bom dia!')
else:
    velocidade >=80 
    multa = float(velocidade - 80)* 7
    print('Você está acima do limite de velocidade e a multa é R$7,00 reais por cada Km acima do limite')
    print(f'Valor da multa é R${multa:.2f}!')