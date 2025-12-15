
print('Olá precisamos de algumas informações para prosseguir')
distancia = float(input('Qual a distância da sua viagem em Km: '))
print(f'Você está prestes a começar uma viagem de {distancia} Km')
if distancia <= 200:
    valor1 = distancia * 0.50
    print(f'O valor da passagem é R${valor1:.2f}')
else :
    valor2 = distancia * 0.45
    print(f'O valor da passagem é R${valor2:.2f}')
    