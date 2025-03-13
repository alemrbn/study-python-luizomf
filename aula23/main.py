# operadores in e not in 
# strings são iteráveis
# 0 1 2 3 4 5
# o t á v i o
#-6-5-4-3-2-1

# nome = 'Otávio'

# print(nome[2])
# print(nome[-4])

# print(10 * '-')

# print('á' in nome)
# print('z' in nome)

# print(10 * '-')

# print('t' not in nome)
# print('e' not in nome)

nome = input('digite seu nome: \n')

encontrar = input('digite o que deseja encontrar: \n')

if encontrar in nome:
  print(f'{encontrar} está em {nome}')
else:
  print(f'{encontrar} não está em {nome}')