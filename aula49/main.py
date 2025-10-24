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

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(0, 5) # argumento 1 recebe o índice, argumento 2 recebe o valor
print(lista)
