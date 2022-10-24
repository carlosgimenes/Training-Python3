# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 027 - Primeiro e último nome de uma pessoa
# Para este Desafio devo ter assistido até a aula 09
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
# último nome separadamente
# Exemplo: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza
# Link para a resolução: https://youtu.be/SifYYsXhLM8
# =================================================================================================

# Como foi resolvido
# 1º Alternativa
nome_completo = str(input('Digite seu nome completo: ')).upper().strip()
nome = nome_completo.split() # O "split" irá fatiar o nome que foi digitado em pedaços separados 
                             # por espaços colocando dentro de uma lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu último nome é {} '.format(nome[len(nome)-1]))

