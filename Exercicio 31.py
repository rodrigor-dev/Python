import math

num = int(input('Digite um número para saber se ele é par ou impar: '))
par = math.fmod(num, 2)
if par == 0:
    print(f'O número que você digitou foi {num} e ele é um número par!')
else :
    par == 1
    print(f'O número que você digitou foi {num} e ele é um número impar!')