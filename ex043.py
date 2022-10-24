# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Desafio 043 - Índice de Massa Corporal
# Para este Desafio devo ter assistido até a aula 12
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
# status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
# Link para a resolução: https://youtu.be/b7r34za963I
# =================================================================================================

# Como fiz
'''peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / ( altura ** 2 )
print("Para o peso de {:.2f} kg e altura de {:.2f} mts o IMC é igual {:.2f}".format(peso, altura, imc))
if imc < 18.5:
  print("Um IMC igual a {:.2f} é classificado como Abaixo do Peso".format(imc))
elif imc >= 18.5 and imc < 25:
  print("Um IMC igual a {:.2f} é classificado como Peso ideal".format(imc))
elif imc >= 25 and imc < 30:
  print("Um IMC igual a {:.2f} é classificado como Sobrepeso, Cuidado!".format(imc))
elif imc >= 30 and imc <= 40:
  print("Um IMC igual a {:.2f} é classificado como Obesidade, recomenda-se procurar apoio médico!".format(imc))
else:
  print("Um IMC igual a {:.2f} é classificado como OBSIDADE MÓRBIDA, é URGENTE a necessidade de apoio médico!".format(imc))'''


# Como foi resolvido
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
