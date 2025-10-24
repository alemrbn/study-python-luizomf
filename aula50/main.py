"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
  append - adiciona um item ao final
  insert - adiciona um item no índice escolhido
  pop - remove do final ou do índice escolhido
  del - apaga um índice
  clear - limpa a lista
  extend - estende a lista
  + - concatena listas
Create Read Update   Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)