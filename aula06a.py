# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 06 - Tipos Primitivos e Saída de Dados
# Link para a aula: https://youtu.be/hdDHg1p3YVc
# =================================================================================================

'''

n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = n1 + n2
print('A soma vale: ', s)

Este exemplo não irá funcionar, pois se por exemplo digitarmos 3 e depois 5, seria mostrado 35 como
resultado, uma vez que ele iria concatenar os doi número digitados. Isto acontece por não termos 
feito uso dos Tipos Primitivos

Fazendo uso do Tipo Primitivo adequado e reescrevendo o programa, teremos:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale: ', s)

'''

'''

Quatro Tipos Primitivos mais básicos do Python são:
int     >>> Números Inteiros Ex.: 7, -4, 0, 9875
float   >>> Números Reais ou de Ponto Flutuante Ex.: 4.5, 0.076, -15.223, 7.0
bool    >>> Valores Lógicos ou Boleanos Ex.: True ou False (O "T" e o "F" devem SEMPRE estar grafados
            em MAIÚSCULO)
str     >>> Valores Caracteres ou String Ex.: 'Olá', '7,5', ''

Para saber o Tipo Primitivo de uma Variável:
    n1 = input('Digite um valor: ')
    print(type(n1))
        Neste caso o "type" fará com que o tipo seja mostrado

Ainda sobre Tipo Primitivo de uma Variável:
    n2 = int(input('Digite outro: '))
        Neste caso (input('Digite outro: '))
            todo conteúdo dos parenteses externo está sendo convertido para o Tipo Inteiro

Mais detalhes:
    n1 = int(input('Digite um valor: '))            
    n2 = int(input('Digite outro: '))
    s = n1 + n2
    print('A soma entre {} e {} vale {}'.format(n1, n2, s))
        Posso ler esta última linha como "A soma entre uma MÁSCARA e outra MÁSCARA vale uma
        terceira MÁSCARA
        Sendo que no .format... eu digo quais são estas MÁSCARAS

Alguns exemplos de Métodos
    n = input('Digite algo:? ')
    print(n.isnumeric())
        Neste exemplo, o "isnumeric" é um MÉTODO, ele irá verificar se é possível converter o que 
        foi digitado em um número com o Tipo Primitivo Inteiro, caso seja, retornará "True"

    print(n.isalpha())
        Neste exemplo, o "isalpha" é um MÉTODO, ele irá verificar se o que foi digitado é letra, 
        caso seja, retornará "True"

    print(n.isalnum())
        Neste exemplo, o "isalnum" é um Método, ele irá verficar se o que foi digitado é alfa 
        numérico, caso seja, retornará "True"

    print(n.isupper())
        Neste exemplo, o "isupper" é um Método, ele irá verificar se o que foi digita está em
        MAIUSCULA, caso esteja, retornará "True"

'''

'''

Forma diferente de escrever o Print

    print('A soma vale', s)     >>> forma como vinhamos escrevendo
    print('A soma vale {}'.format(s))
        neste caso temos o seguinte:
            {} "é uma máscara que será substituida por um método da própria string
            .format(s) é um método
            o "s" que está em .format(s) é o valor que irá aparecer nas chaves "{}"

'''

