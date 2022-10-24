# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 026 - Primeira e última ocorrência de uma string
# Para este Desafio devo ter assistido até a aula 09
# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez
# Link para a resolução: https://youtu.be/WHWGz2Dy1ZU
# =================================================================================================

# Como foi resolvido
# 1º Alternativa
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
