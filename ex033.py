# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 033 - Maior e menor valores
# Para este Desafio devo ter assistido até a aula 10
# Faça um programa que leia três números e mostre qual é MAIOR e qual é o MENOR
# Link para a resolução: https://youtu.be/a_8FbW5oH6I
# =================================================================================================


# Como fiz:
# Tive dificuldade com a lógica
'''valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))

print('Primeiro valor digitado: {}'.format(valor1))
print('Segundo valor digitado: {}'.format(valor2))
print('Terceiro valor digitado: {}'.format(valor3))'''


# Como foi resolvido
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
