# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 11 - Cores no Terminal
# Link para a aula: https://youtu.be/0hBIhkcA8O8
# =================================================================================================

'''
Padrão ANSI escape sequence

Sempre que quiser representar uma cor em Python, devemos começar escrevendo:
\033[Style;Text;Backm

Exemplo
\033[0;33;44m

Style               Text                Back
0 None              30 Branco           40 Fundo Branco  
1 Bold              31 Vermelho         41 Fundo Vermelho
4 Underline         32 Verde            42 Fundo Verde   
7 Negative          33 Amarelo          43 Fundo Amarelo        \033[0;33;44m]
                    34 Azul             44 Fundo Azul    
                    35 Magenta          45 Fundo Magenta 
                    36 Ciano            46 Fundo Ciano   
                    37 Cinza            47 Fundo Cinza   
'''

# EXERCÍCIOS

'''print('\033[31mOlá, Mundo!')'''
'''print('\033[1;31;43mOlá, Mundo!')'''
'''print('\033[30mOlá, Mundo!\033[m')'''

'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
'''

'''
nome = 'Gimenes'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;31m', nome, '\033[m'))
'''

nome = 'Jaqueline'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))