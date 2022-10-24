# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 034 - Aumentos múltiplos
# Para este Desafio devo ter assistido até a aula 10
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# Link para a resolução: https://youtu.be/Sfadj_AzKHw
# =================================================================================================

# Como fiz:
'''salario = float(input('Informe o salário atual: R$'))
if salario > 1250:
  salariomaior = salario * 1.10
  print('O novo salário será de R$ {:.2f}'.format(salariomaior))
if salario <= 1250:
  salariomenor = salario * 1.15
  print('O novo salário será de R$ {:.2f}'.format(salariomenor))'''


# Como foi resolvido
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar agora R${:.2f}'.format(
    salario, novo))
