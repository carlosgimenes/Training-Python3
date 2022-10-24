# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Desafio 037 - Conversor de Bases Numéricas
# Para este Desafio devo ter assistido até a aula 12
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão:
# . 1 para binário
# . 2 para octal
# . 3 para hexadecimal
# Link para a resolução: https://youtu.be/B3F0IjH5WAM
# =================================================================================================

# Como fiz
'''numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    binary = bin(numero)
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, binary))
elif base == 2:
    octal = oct(numero)
    print('{} convertido para OCTAL é igual a {}'.format(numero, octal))
else:
    hexa = hex(numero)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hexa))'''


# Como foi resolvido
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convetido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convetido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(
        num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
