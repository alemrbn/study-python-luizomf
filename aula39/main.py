"""calculadora com while"""

def read_number(message):
    while True:
        entry = input(message)
        try:
            # Primeiro tenta converter para int
            value = int(entry)
            return value
        except ValueError:
            try:
                # Se falhar, tenta converter para float
                value = float(entry)
                return value
            except ValueError:
                # Se falhar para int e float, retorna inválido
                print("\n*Número inválido!\n")

def subtraction(n1, n2):
  result = n1 - n2
  return result

def division(n1, n2):
  result = n1 / n2
  return result

def multiplication(n1, n2):
  result = n1 * n2
  return result

while True:
  n1 = read_number('Digite o primeiro número: ')
  operator = input('Digite o operador (+ - / *): ')
  n2 = read_number('Digite o segundo número: ')

  # valid_numbers = None

  # try:
  #   n1_float = float(n1)
  #   n2_float = float(n2)
  #   valid_numbers = True
  # except:
  #   valid_numbers = None

  # if valid_numbers is None:
  #   print('\n*Um ou ambos os números são inválidos!\n')
  #   continue

  if operator == '+':
    print('\nResultado:', sum([n1, n2]))
  elif operator == '-':
    print('\nResultado:', subtraction(n1, n2))
  elif operator == '/':
    print('\nResultado:', division(n1, n2))
  elif operator == '*':
    print('\nResultado:', multiplication(n1, n2))
  else:
    print('\n*Operador inválido!\n')
    continue

  bye = input('\n*Deseja encerrar? [s]im, [n]ão ').lower()

  if bye in ['s', 'sim']:
    print('\n*Encerrando...\n')
    break
  elif bye in ['n', 'não', 'nao']:
    continue
  else:
    print('\n*Resposta inválida! encerrando...\n')
    break
