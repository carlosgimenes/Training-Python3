# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 04 - Primeiros comandos em Python3
# Link para a aula: https://youtu.be/31llNGKWDdo
# =================================================================================================

'''
Delimitador padrão mensagens >>> 'Aspas Simples'

Delimitador Função >>> print('Olá, Mundo!')
    Neste exemplo temos o seguinte:
        - print     = Função
        - "()"      = Delimitador

Ao escrever números = sem aspas
Ao escrever texto   = colocar aspas

print('Olá, Mundo!')
    - Leia-se: escreva na tela Olá, Mundo!

No Python, não estando entre aspas
    - Escreva SEMPRE em letras MINÚSCULAS

No Python, toda variável é um OBJETO

Toda variável pode receber valores e esse "recebe" é simbolizado pelo sinal de "=" 

nome    = 'Gimenes'         Leia-se:    nome    recebe "Gimenes"
idade   = 25                            idade   recebe "25"
peso    = 75.8                          peso    recebe "75.8"

Vamos mostrar estes valores na tela, utilizando a função "print" da seguinte forma:

    - print(nome, idade, peso)

Criando uma interatividade com o usuário, fazendo uso da função "input"
    nome = input('Qual é seu nome?' )           >>> Leia-se: nome recebe o resultado de input de Qual é o seu nome?
    idade = input('Quantos anos você tem? ')    >>> Leia-se: idade recebe o resultado de input de Quantos anos você tem?
    peso = input('Quanto você pesa? ')          >>> Leia-se: peso recebe o resultado de input de Quanto você pesa?
    print(nome, idade, peso)

Via de regra, todo script Python, tem extensão ".py"

Resumo desta aula:
    - como usar "print"
    - como usar variáveis
    - como atribuir valor a variáveis utilizando recebe "="
    - como mostrar variáveis utilizando print com "," e "+"
    - como utilizar "input" para interagir com usuário
    - como criar script separados para utilizar posteriormente

'''

# Exemplos

print('7'+'4')

print(7 + 4)

nome = 'Carlos'
idade = 59
peso = 90.4

print( nome, idade, peso )

nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual é o seu peso? ')
print(nome, idade, peso)