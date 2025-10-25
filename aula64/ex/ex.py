CPF = '746.824.890-70'

def get_first_nine_digits(cpf):
  first_nine_digits = cpf.split('-')[0].replace('.', '')
  return first_nine_digits

def get_cpf_digit(cpf_digits, start_weight):
  multiplication_result = []
  weights = list(range(start_weight, 1, -1))
  for i in range(len(cpf_digits)):
    digit = int(cpf_digits[i])
    weight = weights[i]
    multiplication_result.append(digit * weight)
  total = sum(multiplication_result) * 10
  total = total % 11
  digit = 0 if total > 9 else total
  return digit

def get_full_cpf(cpf):
  first_nine_digits = get_first_nine_digits(cpf)
  first_digit = get_cpf_digit(first_nine_digits, 10)
  ten_digits = first_nine_digits + str(first_digit)
  second_digit = get_cpf_digit(ten_digits, 11)
  full_cpf = ten_digits + str(second_digit)
  return full_cpf

def cpf_validation(user_cpf):
  clean_cpf_numbers = str(user_cpf).replace('.', '').replace('-', '')
  first_nine_digits = clean_cpf_numbers[:9]
  full_cpf_calculated = get_full_cpf(first_nine_digits)

  check_repeated_characters = user_cpf[0] == user_cpf[0] * len(user_cpf)

  if check_repeated_characters:
    print('CPF Inválido!')
    return False

  if clean_cpf_numbers == full_cpf_calculated:
    print('CPF Válido!')
    return True
  else:
    print('CPF Inválido!')
    return False

