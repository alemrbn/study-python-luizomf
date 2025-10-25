import os

def start():
  messages = {
    'select_option': 'Selecione uma opção:\n',
    'invalid_select_option': 'Selecione uma opção válida!\n',
    'list_items_empty': 'Sua lista não tem nenhum item.\n',
    'user_item_list': 'Item: ',
    'user_options': '[i]nserir, [a]pagar, [l]istar, [s]air\n\n',
    'user_options_error': 'Opção inválida!\n',
    'select_index_delete': 'Qual índice deseja apagar? ',
    'select_index_delete_error': 'Selecione um índice válido!\n',
    'select_index_delete_success': 'Item deletado com sucesso!\n'
  }

  def clear_screen():
    system = os.name

    if system == 'nt':
      os.system('cls')
    else:
      os.system('clear')
  
  def get_user_option():
    print(messages['select_option'])
    user_option = input(messages['user_options'])
    user_option_lower = user_option.lower()

    return user_option_lower

  def create_list():
    user_list_item = input(messages['user_item_list'])
    user_list_item_capitalize = user_list_item.capitalize()
    list_items.append(user_list_item_capitalize)

  def delete_list_item():
    user_item_index = input(messages['select_index_delete'])
    
    try:
      user_item_index_int = int(user_item_index)

      if user_item_index_int >= len(list_items) or user_item_index_int < 0:
        clear_screen()
        print(messages['select_index_delete_error'])
      else:
        clear_screen()
        list_items.pop(user_item_index_int)
        print(messages['select_index_delete_success'])
    except (ValueError, IndexError):
      clear_screen()
      print(messages['select_index_delete_error'])
  
  def show_list():
    for index, item in enumerate(list_items):
      print(index, item)
    print()

  def check_list():
    if len(list_items) == 0:
      clear_screen()
      print(messages['list_items_empty'])
      return False
    return True

  list_items = []
  
  while True:
    get_user_option_value = get_user_option()

    if get_user_option_value.isdigit():
      clear_screen()
      print(messages['user_options_error'])
      continue
    
    if get_user_option_value in ['s', 'sair']:
      clear_screen()
      exit()
    elif get_user_option_value in ['i', 'inserir']:
      clear_screen()
      create_list()
      clear_screen()
    elif get_user_option_value in ['a', 'apagar']:
      if not check_list():
        continue
      else: 
        clear_screen()
        show_list()
        delete_list_item()
    elif get_user_option_value in ['l', 'listar']:
      if not check_list():
        continue
      else:
        clear_screen()
        show_list()
    else:
      clear_screen()
      print(messages['invalid_select_option'])
      continue
    
      

