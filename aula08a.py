# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 08 - Utilizando Módulos
# Link para a aula: https://youtu.be/oOUyhGNib2Q
# =================================================================================================

# 1º Exemplo
# Neste exemplo importamos todas as funcionalidades do Módulo
import math
from sys import float_repr_style
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))

# 2º Exemplo
# Neste exemplo importamos apenas a funcionalidade Raiz Quadrada
from math import sqrt, floor
num = int(input('Digite um número '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# Para saber as Bibliotecas que eu posso importar, posso consultar em 
# python.org

# 3º Exemplo
import random
numero = random.randint(1, 10)
print(numero)

# 4º Exemplo
import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))