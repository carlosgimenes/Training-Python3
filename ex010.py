# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 010 - Conversor de Moedas
# Para este Desafio devo ter assistido até a aula 07
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela
# pode comprar. Considere US$1,00 = R$3,27
# Link para a resolução: https://youtu.be/xM4AX3Lp2mo
# =================================================================================================

# Como fiz:
real = float(input('Informe quantos reais você tem: '))
t = real / 3.27
print('Com esse valor você pode comprar {:.2f} Dolares'.format(t))

# Como foi resolvido
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dollar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dollar))