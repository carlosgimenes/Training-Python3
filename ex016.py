# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 016 - Quebrando um número
# Para este Desafio devo ter assistido até a aula 08
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção 
# inteira.
# Exemplo: Digite um número: 6,127 O número 6,127 tem a parte inteira 6
# Link para a resolução: https://youtu.be/-iSbDpl5Jhw
# =================================================================================================

# Como fiz:
'''from math import floor
numero = float(input('Digite um número: '))
print('O número {} tem a parte inteira igual a {}'.format(numero, floor(numero)))'''


# Como foi resolvido
# 1º Alternativa
'''import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))'''

# 2º Alternativa
'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

# 3º Alternativa
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))