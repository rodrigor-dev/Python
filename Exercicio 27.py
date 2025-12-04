'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a ultima vez.'''

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Na frase {frase.title()} tem {frase.count('A')} letras "A"')
print(f'Aparece a primeira vez na posição:{frase.find('A')+1}')
print(f'Aparece a ultima vez na posição:{frase.rfind('A')+1}')
