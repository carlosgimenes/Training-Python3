# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 025 - Procurando uma string dentro de outra
# Para este Desafio devo ter assistido até a aula 09
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
# Link para a resolução: https://youtu.be/WHWGz2Dy1ZU
# =================================================================================================

# Como foi resolvido
# 1º Alternativa
# Para resolução deste execício usaremos o OPERADOR "in"
nome = str(input('Qual é o seu nome completo? ')).strip() # O MÉTODO strip irá remover espaços em branco
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # O lower irá passar o texto para Minúscula para comparar

