# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 022 - Analisador de Textos
# Para este Desafio devo ter assistido até a aula 09
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas
# 2. O nome com todas as letras minúsculas
# 3. Quantas letras ao todo (sem considerar espaços)
# 4. Quantas letras tem o primeiro nome
# Link para a resolução: https://youtu.be/EQQt-6QqXOs
# =================================================================================================

# Como fiz:
# Não consegui resolver o item 3 e item 4

'''
nome = str(input('Qual é o seu nome completo: '))
print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))
# print('O nome tem um total de {} letras').format(nome.lower(''.join(nome)))
#print('Total de letras do primeiro nome {}'.format(len(nome)))
'''


# Como foi resolvido
# 1º Alternativa
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''


# Como foi resolvido
# 2º Alternativa
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))