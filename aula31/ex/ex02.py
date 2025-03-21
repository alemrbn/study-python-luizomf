def greeting():
  entry = input('Que horas são? \n')

  if entry.isdigit():
    hours = int(entry)

    if hours >= 0 and hours <= 11:
      print('Bom dia!')
    elif hours >= 12 and hours <= 17:
      print('Boa tarde!')
    elif hours >= 18 and hours <= 4:
      print('Boa noite!')
    else:
      print('Hora inválida!')

  else: 
    print('Digite apenas números!')
    return
