from math import fmod
from datetime import date

ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
bi = fmod(ano, 4) 
if bi == 0 and fmod(ano, 100) != 0 or fmod(ano, 400) == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto!')