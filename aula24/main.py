"""
interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %06X' % (15, 15))
