# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 019 - Sorteando um item na lista
# Para este Desafio devo ter assistido até a aula 08
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que 
# ajude ele, lendo o nome deles e escrevendo o nome do escolhido
# Link para a resolução: https://youtu.be/_Nk02-mfB5I
# =================================================================================================

# Como fiz:
'''
import random
aluno = random.choice( ['João', 'Maria', 'José', 'Magali'] )
print(aluno)
'''

# Como foi resolvido
# 1º Alternativa
'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''

# Como foi resolvido
# 2º Alternativa
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))