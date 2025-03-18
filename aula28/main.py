"""
introdução ao try/except
try -> tente executar o código
except -> ocorreu algum erro ao tentar executar o código
"""

numero_str = input('Vou dobrar o número que você digitar: \n')

try:
  print(type(numero_str), 'STR:', {numero_str})
  numero_float = float(numero_str)
  print(type(numero_float), 'FLOAT:', {numero_str})
  print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
  print('Você precisa digitar um número.')

# if not numero_str.isdigit():
#   numero_float = float(numero_str)
#   print('Você precisa digitar um número.')
# else:
#   print(f'O dobro de {numero_str} é {numero_float * 2}')
