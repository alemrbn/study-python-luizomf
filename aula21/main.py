# operadores lógicos
# and (e) or (ou) (not) não
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso, a expresão inteira será avaliada naquele valor
# são considerados falsy: 0 0.0 '' False
# também existe o tipo none que é usado para representar um não valor

# entrada = input('[E]ntrar | [S]air\n')
# senha = input('Senha:\n')
# senha_permitida = '123'

# if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
#   print('você entrou!')
# else:
#   print('saindo..')

# avaliação de curto circuito
# print(True or 0 or True)

senha = input('Senha') or 'você não digitou a senha'
print(senha)
