# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 07 - Operadores Aritméticos
# Link para a aula: https://youtu.be/Vw6gLypRKmY
# =================================================================================================

'''
Operadores Aritiméticos
    +   Adição
    -   Subtração
    *   Multiplicação
    /   Divisão
    **  Potência
    //  Divisão Inteira
    %   Resto da Divisão

'''

'''
Ordem de Precedência
    1a ()               >>> Tem parenteses, resolve primeiro
    2a **               >>> Exponenciação é a segunda ordem de precedência
    3a * / // %         >>> Neste caso resolvo aquele que aparecer primeiro
    4a + -              >>> Por último resolvemos a soma e a subtração

'''

# Exemplos

'''
5 + 3 * 2 == 11
    Neste exemplo, de acordo com a ordem de precedência, devemos fazer primeiro a multiplicação
    para depois fazer a soma, desta forma 3 * 2 = 6, que somado a 5 será igual a 11

'''

'''
3 * 5 + 4 ** 2 == 31
    Neste exemplo, de acordo com a ordem de precedência, devemos fazer primeiro a Exponenciação,
    para depois fazer a multiplicação e em seguida a soma, desta forma 4 ** 2 = 16, 3 * 5 = 15,
    agora somando 15 + 16 teremos 31 como resultado final

'''

'''
3 * ( 5 + 4 ) ** 2 == 243
    Neste exemplo, de acordo com a ordem de precedência, devemos resolver primeiro o pareteses, 
    para então fazer a Exponenciação, para depois fazer a multiplicação, desta forma 5 + 4 = 9
    que elevado ao quadrado dá 81 e multiplicado por 3 teremos 243 como resultado final

'''


# Prática
'''
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))