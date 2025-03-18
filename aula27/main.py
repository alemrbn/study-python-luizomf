"""
exercício
peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade

se nome e idade forem digitados:
  Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letras}
    A última letra do seu nome é {letra}
se nada for digitado em seu nome ou idade:
  exiba "Desculpe, você deixou campos vazios"
"""

name = input('Digite seu nome: \n')
age = input('Digite sua idade: \n')

def name_invert(var):
  var = var[-1::-1]
  return var

def check_spaces(var):
  spaces = var.count(' ')
  return spaces

def remove_spaces(var):
  var = var.replace(' ', '')
  return len(var)

if not name or not age:
  print('Desculpa, você deixou campos vazios!')
else:
  print(f'Seu nome é: {name}')
  print(f'Sua idade é: {age}')
  print(f'Seu nome invertido é: {name_invert(name)}')
  print(f'Seu nome contém {check_spaces(name)} espaços')
  print(f'Seu nome contém {remove_spaces(name)} letras')
  print(f'A primeira letra do seu nome é: {name[0]}')
  print(f'A última letra do seu nome é: {name[-1]}')
