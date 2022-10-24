# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 018 - Seno Coseno e Tangente
# Para este Desafio devo ter assistido até a aula 08
# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente 
# desse ângulo
# Link para a resolução: https://youtu.be/9GvsphwW26k
# =================================================================================================

# Como fiz:
'''
import math
angulo = float(input('Informe o valor do ângulo para ser calculado: '))
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O ângulo de {:.4f}° tem um valor de seno igual a {:.4f}, um valor de coseno igual a  {:.4f} e um valor de tangente igual a {:.4f}'.format(angulo, seno, coseno, tangente))
'''


# Como foi resolvido
# 1º Alternativa
'''
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
'''

# Como foi resolvido
# 2º Alternativa
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
coseno = cos(radians(angulo))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))