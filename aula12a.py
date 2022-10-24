# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Aula 12 - Condições Aninhadas
# Link para a aula: https://youtu.be/j9bYDjaAYzw
# =================================================================================================

'''
ATENÇÃO com os dois pontos no final 

Estrutua aninhada padrão

if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
else:
    bloco3


Dentro de um if posso ter quantos elif eu precisar

if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.re():
    bloco3
else:
    bloco4
'''

# EXERCÍCIOS
# =================================================================================================

# Estrutura condicional simples
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gimenes':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))'''


# Estrutura condicional composta
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gimenes':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))'''


# Estrutura condicional aninhada
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gimenes':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))'''

# Outro exemplo Estrutura condicional aninhada
nome = str(input('Qual é o seu nome? '))
if nome == 'Gimenes':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Elenilza Jaqueline Heloisa':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))