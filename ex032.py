# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 032 - Ano Bissexto
# Para este Desafio devo ter assistido até a aula 10
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
# Link para a resolução: https://youtu.be/cyGY_83m4Xw
# =================================================================================================

# Como fiz:
# Para verificar se um ano é bissexto em Python, basta importar o módulo "calendar". Ele possuí uma
# função chamada "isleap", que retorna "True" se o ano for bissexto

'''
from calendar import isleap

ano = int(input('Informe o ano a ser pesquisado: '))
if isleap(ano):
    print('O ano de {} é um ano Bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto!'.format(ano))
'''


# Como foi resolvido
# 1º Alternativa
'''ano = int(input('Que ano quer analisear? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
'''


# 2º Alternativa
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year     # Irá pegar o Ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))