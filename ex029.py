# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 029 - Radar Eletrônico
# Para este Desafio devo ter assistido até a aula 10
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite
# Link para a resolução: https://youtu.be/hgJ_ETNGSj8
# =================================================================================================

# Como fiz:

'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
print('Velocidade informada: {} Km/hora '.format(velocidade))
if velocidade > 80:
    print('Você excedeu o limite de velocidade')
    print('Você foi multado em R${:.2f} Tenha mais CUIDADO!'.format(multa))
else:
    print('Você está dentro dos limites de velocidade, Parabens!')
'''


# Como foi resolvido

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com SEGURANÇA')