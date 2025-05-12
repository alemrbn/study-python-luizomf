"""
iterando strings com while
"""

#       012345678910
nome = 'Luiz Otávio'
#      1110987654321
tamanho_nome = len(nome)

indice = 0
novo_nome = ''

while indice < tamanho_nome:
  print(f'Caractere: {nome[indice]} | Índice: {indice}')
  letra = nome[indice]
  novo_nome += letra
  indice += 1
