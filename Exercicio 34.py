print('Fale três números para saber qual é o maior e o menor entre eles')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceeiro número: '))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f'Os números são {num1}, {num2}, {num3}.')
print(f'O maior número entre eles é {maior} e o menor é {menor}!')