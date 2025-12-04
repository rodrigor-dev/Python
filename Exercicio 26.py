'''Crie um Programa que leia o nome completo de uma pessoa e diga se tem Silva'''
nome = str(input('Digite seu nome completo: ')).strip()
print(f'O seu nome tem SILVA? {'SILVA' in nome.upper()}')