valor = float(input('Qual o valor do produto? R$'))
novo = valor - (valor * 5 / 100)
print(f'O valor do produto que era R${valor:.2f}, na promoção com 5% de desconto será: R${novo:.2f}')
