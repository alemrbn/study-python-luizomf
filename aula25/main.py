"""
formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes dos zeros
sinal - + ou -
Ex.: 0>-100,.1f
conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:.^10}')
print(f'{1000.4873648123746:0>+10,.1f}')

print(10 * '-')

print(f'o hexadecimal de 15 é {15:06X}')

