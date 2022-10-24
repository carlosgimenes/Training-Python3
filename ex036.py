# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Desafio 036 - Aprovando Empréstimo
# Para este Desafio devo ter assistido até a aula 12
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
# empréstimo será negado
# Link para a resolução: https://youtu.be/IV13X0QOMU8
# =================================================================================================

# Como fiz
'''casa = float(input('Informe o valor de venda do imóvel: R$'))
salario = float(input('Informe o salário do comprador: R$'))
anos = int(input('Informe em quantos anos deseja pagar: '))

prestacao = casa / (anos * 12)
teto = salario * (30 / 100)

if teto <= prestacao:
    print('Para uma casa no valor R${:.2f} a ser paga em {} anos, a prestação será de R${:.2f}'.format(
        casa, anos, prestacao))
    print('Empréstimo NEGADO!')
else:
    print('Para uma casa no valor R${:.2f} a ser paga em {} anos, a prestação será de R${:.2f}'.format(
        casa, anos, prestacao))
    print('PARABÉNS, seu financiamento foi aprovado!')'''


# Como foi resolvido
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
