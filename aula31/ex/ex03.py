def name_info():
  entry = input('Digite o seu primeiro nome: \n')

  if len(entry) <= 4:
    print('Seu nome é curto.')
  elif len(entry) <= 6:
    print('Seu nome é normal.')
  else:
    print('Seu nome é muito grande')

