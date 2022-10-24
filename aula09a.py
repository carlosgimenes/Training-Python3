# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Aula 09 - Manipulando Texto
# Link para a aula: https://youtu.be/a7DH88vk2Sk
# =================================================================================================

# Escrever a Frase
'''
frase = 'Curso em Vídeo Python'
print(frase)
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar a quarta letra da frase
'''
frase = 'Curso em Vídeo Python'
print(frase[3])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar da quarta letra até a letra treze da frase
# Lembre-se que a contagem inicia-se em "0"
'''
frase = 'Curso em Vídeo Python'
print(frase[3:13])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar do início até a letra treze da frase
'''
frase = 'Curso em Vídeo Python'
print(frase[:13])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar da letra treze até o final da frase
'''
frase = 'Curso em Vídeo Python'
print(frase[13:])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar da letra um até a letra quinze
'''
frase = 'Curso em Vídeo Python'
print(frase[1:15])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar da letra um até a letra quinze, pulando de dois em dois
'''
frase = 'Curso em Vídeo Python'
print(frase[1:15:2])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar da letra um até o final, pulando de dois em dois
'''
frase = 'Curso em Vídeo Python'
print(frase[1::2])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar letras do início até o final, pulando de dois em dois
'''
frase = 'Curso em Vídeo Python'
print(frase[::2])
'''

# Fatiando a Frase
# Neste exemplo queremos mostrar quantas letras "o" existem na frase
'''
frase = 'Curso em Vídeo Python'
print(frase.count('o'))
'''

# Fatiando a Frase
# Neste exemplo queremos passar a frase inteira para maiusculas e depois saber quantas letras "O" 
# existem na frase
'''
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
'''

# Fatiando a Frase
# Neste exemplo queremos saber o tamanho da frase
'''
frase = 'Curso em Vídeo Python'
print(len(frase))
'''

# Fatiando a Frase
# Neste exemplo queremos remover os espaços existentes no início e fim da frase e mostrar seu tamanho
# após isso
'''
frase = '   Curso em Vídeo Python  '
print(len(frase.strip()))
'''

# Fatiando a Frase
# Neste exemplo queremos trocar a palavra Python por Android
'''
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
'''

# Fatiando a Frase
# Neste exemplo queremos saber se a palavra Curso aparece na frase
'''
frase = 'Curso em Vídeo Python'
print('Curso' in frase)
'''

# Fatiando a Frase
# Neste exemplo queremos saber em que posição a palavra Curso aparece
'''
frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))
'''

# Fatiando a Frase
# Neste exemplo queremos transformar a frase em lista
'''
frase = 'Curso em Vídeo Python'
print(frase.split())
'''