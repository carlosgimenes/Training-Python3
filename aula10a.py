# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 10 - Condições (Parte 1)
# Link para a aula: https://youtu.be/K10u3XIf1-Q
# =================================================================================================

'''
Condição

se carro.esquerda()
    bloco _V_
senão
    bloco _F_


if carro.esquerda():
    bloco True
else:
    bloco False

Exemplo1:
tempo = int(input('Quantos anos tem seu carro?))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

Lembre-se: 
    > todo comando que estiver alinhado a esquerda, será executado SEMPRE
    > todo comando que estiver ANINHADO, OU SEJA, COM INDENTAÇÃO, ele pode ser executado ou não

Exemplo2:
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

'''

# EXERCÍCIOS


# Estrutura condicional simples
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gimenes':
    print('Que nome lindo você tem!')
print('Bom dia, {}'.format(nome))'''

# Estrutura condicional composta
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gimenes':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!!')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ( n1 + n2 ) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')