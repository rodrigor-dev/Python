'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.


O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

n = int(input('Tente descobrir um número de 0 a 5 que estou "pensando": ')) #Jogador tenta adivinhar
sorte = randint(0, 5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Processando ...')
print('-=-'*20)
sleep(3)
if sorte == n:
    print(f'PARABENS! Você venceu!')
else :
    print(f'GANHEI ! Eu pensei no número {sorte} e não no {n}!')