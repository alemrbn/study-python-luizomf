"""
Como o for funciona por de baixo dos panos

Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
#   print(letra)
texto = 'Luiz' # iterável
iterator = iter(texto) # iterator

while True:
  try:
    letra = next(iterator)
    print(letra)
  except StopIteration:
    break

# texto = iter('luiz') # __iter__()

# print(next(texto)) # __next__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()