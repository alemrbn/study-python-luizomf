"""
fatiamento de strings
 012345678
 olá mundo
-987654321
fatiamento [início:fim:passo] [::]
obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'olá mundo'

print(variavel[5]) # retorna o índice 5 da string
print(variavel[4:]) # retorna a string inteira a partir do índice 4
print(variavel[4:8]) # retorna a string a partir do índice 4 até o 7 (omitindo o índice 8)
print(variavel[0:5]) # retorna a string a partir do índice 0 até o 4 (omitindo o índice 5)
print(variavel[:5]) # retorna a string inteira até o índice 5
print(len(variavel)) # retorna o tamanho da string (quantos caracteres a string possui)
print(variavel[0:len(variavel):1]) # retorna a string inteira
print(variavel[::-1]) # invertendo a string ( print(variavel[-1:-10:-1]) )
