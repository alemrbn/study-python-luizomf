import os

def start():
  def clear_screen():
    system = os.name
    
    if system == 'nt': #windows
      os.system('cls')
    else:
      os.system('clear')

  print('Bem vindo ao jogo!\n')
  secret_word = 'motocicleta'
  found_letters = ''
  attempts = 1

  while True: 
    entry = input('Digite uma letra: ')
    if len(entry) > 1 or entry.isdigit():
      print('Digite apenas uma letra!')
      continue
    if entry in secret_word:
      found_letters += entry
      #print(found_letters) test

    secret_word_hidden = ''

    for letter in secret_word:
      if letter in found_letters:
        secret_word_hidden += letter
      else:
        secret_word_hidden += '*'
    
    print(secret_word_hidden)

    if secret_word_hidden == secret_word:
      clear_screen()
      print('\nPARABÉNS, VOCÊ GANHOU!\nTentativas: ', attempts, '\n')
      break
    
    attempts += 1
    