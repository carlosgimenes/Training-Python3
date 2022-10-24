# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 020 - Sorteando uma ordem na lista
# Para este Desafio devo ter assistido até a aula 08
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos 
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
# Link para a resolução: https://youtu.be/OPh0nngbBSY
# =================================================================================================

# Como fiz:
'''
import random
aluno1 = str(input('Informe o nome do 1o aluno: '))
aluno2 = str(input('Informe o nome do 2o aluno: '))
aluno3 = str(input('Informe o nome do 3o aluno: '))
aluno4 = str(input('Informe o nome do 4o aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação dos trabalhos será: ')
print(lista)
'''

# Como foi resolvido
# 1º Alternativa
'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista =  [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
'''

# Como foi resolvido
# 2º Alternativa
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)