# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 031 - Custo da Viagem
# Para este Desafio devo ter assistido até a aula 10
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200 Km e R$0,45 para viagens mais longas
# Link para a resolução: https://youtu.be/PGqHyzWoagc
# =================================================================================================

# Como fiz:

'''
distancia = float(input('Informe a distância de sua viagem em Km: '))

if distancia <= 200:
    valor1 = (distancia * 0.50)
    print('O valor da sua passagem será de R${:.2f}'.format(valor1))
else:
    valor2 = (distancia * 0.45)
    print('O valor da sua passagem será de R${:.2f}'.format(valor2))
'''


# Como foi resolvido
# 1º Alternativa
'''
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
'''


# Como foi resolvido
# 2º Alternativa (Fazendo uso do "if" simplificado)
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))