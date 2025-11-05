altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
tinta = (altura * largura)/2
area = altura * largura
print(f'Sua parede tem a dimensão de {altura}x{largura} e sua area é de {area}m².')
print(f'Para pintar essa parede, você irá utilizar {tinta}l de tinta ! ')