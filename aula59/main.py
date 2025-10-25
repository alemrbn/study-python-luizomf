"""
split e join com list e str
split - divide uma string (return list)
join - une uma string
"""

frase = '           Olha só que     ,    coisa interessante      '
lista_frases_cruas = frase.split(', ')

lista_frases_fixed = []
for i, frase in enumerate(lista_frases_cruas):
  lista_frases_fixed.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases_fixed)

frases_unidas = ', '.join(lista_frases_fixed)
print(frases_unidas)
