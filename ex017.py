# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 017 - Catetos e Hipotenusa
# Para este Desafio devo ter assistido até a aula 08
# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo 
# retângulo, calcule e mostre o comprimento da hipotenusa
# Link para a resolução: https://youtu.be/vmPW9iWsYkY
# =================================================================================================

# Como fiz:
'''oposto = float(input('Informe a medida do cateto oposto: '))
adjacente = float(input('Informe a medida do cateto adjascente: '))
hipotenusa = (oposto**2 + adjacente**2)**(1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''

# Como foi resolvido
# 1º Alternativa
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''


# Como foi resolvido
# 2º Alternativa
import math
from traceback import print_tb
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))