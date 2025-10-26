"""
Argumentos nomeados e não nomeados com funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
  # definição
  print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

# execução
soma(5, 5, 2) # argumento não nomeado
soma(y=2, z=3, x=15) # argumento nomeado
