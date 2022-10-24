# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 002 - Respondendo ao Usuário
# Para este Desafio devo ter assistido até a aula 04
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas
# Link para a resolução: https://youtu.be/FNqdV5Zb_5Q
# =================================================================================================

# Como fiz:
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

'''
Detalhes sobre a saída formatada:
    - {} >>> Este bloco será substituido pela formatação
    - .format(nome) >>> aqui o "nome" será formatado para caber dentro do {}
'''