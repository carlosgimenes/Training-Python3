# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 023 - Separando dígitos de um número
# Para este Desafio devo ter assistido até a aula 09
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex. Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
# Link para a resolução: https://youtu.be/wD2aerLMBWA
# =================================================================================================

# Como fiz:
# Não consegui resolver
'''
numero = str(input('Informe um número: '))
lista = numero.split()
print(lista[0])
'''


# Como foi resolvido
# 1º Alternativa (Esta solução para funcionar o número informado precisa obrigatoriamente ser uma milhar)
'''
num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
'''

# Como foi resolvido
# 2º Alternativa
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))