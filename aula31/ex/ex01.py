def check_number():
  try:
    number = int(input('Digite um número inteiro: \n'))
  except ValueError:
      print('Digite apenas números inteiros')
      return

  if number % 2 == 0:
    print(f'O número {number} é par')
  else:
    print(f'O número {number} é impar')
