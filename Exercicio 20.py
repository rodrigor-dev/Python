#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
a1 = input('Digite o nome do Primeiro Aluno: ')
a2 = input('Digite o nome do Segundo Aluno: ')
a3 = input('Digite o nome do Terceiro Aluno: ')
a4 = input('Digite o nome do Quarto Aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}!')