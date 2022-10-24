# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 012 - Calculando Descontos
# Para este Desafio devo ter assistido até a aula 07
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
# Link para a resolução: https://youtu.be/4MAmKOT9FeU
# =================================================================================================

# Como fiz:
preco = float(input('Informe o preço normal do Produto: '))
desconto = preco * 0.95
print('O preço de Produto com desconto é {:.2f}'.format(desconto))

# Como foi resolvido
preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 /100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))
