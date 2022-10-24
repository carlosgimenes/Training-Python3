# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 015 - Aluguel de Carros
# Para este Desafio devo ter assistido até a aula 07
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro e a quantidade de 
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por 
# dia e R$0,15 por km rodado
# Link para a resolução: https://youtu.be/I4NYUeetLAc
# =================================================================================================

# Como fiz:
km = float(input('Informe a Km percorrida: '))
dias = int(input('Informe o número de dias de aluguel: '))
preco = 0.15 * km + 60 * dias

print('O valor total do aluguel a pagar é de R${:.2f}'.format(preco))

# Como foi resolvido
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O toal a pagar é de R${:.2f}'.format(pago))