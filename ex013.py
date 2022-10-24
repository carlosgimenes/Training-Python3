# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 013 - Reajuste Salarial
# Para este Desafio devo ter assistido até a aula 07
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% 
# de aumento
# Link para a resolução: https://youtu.be/cTkivN8XcJ0
# =================================================================================================

# Como fiz:
salario = float(input('Informe o sálario atual: '))
reajuste = salario * 1.15
print('O novo sálario é de {:.2f}, parabéns pelo reajuste!'.format(reajuste))

# Como foi resolvido
salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))