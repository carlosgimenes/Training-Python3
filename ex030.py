# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 030 - Par ou Ímpar?
# Para este Desafio devo ter assistido até a aula 10
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
# Link para a resolução: https://youtu.be/4vFCzKuHOn4
# =================================================================================================

# Como fiz:

'''
numero = int(input('Informe um número inteiro: '))
if (numero%2) == 0:
    print('O número {} digitado é PAR'.format(numero))
else:
    print('O número {} digitado é ÍMPAR'.format(numero))
'''


# Como foi resolvido

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))