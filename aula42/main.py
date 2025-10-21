# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_digitada != senha_salva:
#   senha_digitada = input(f'Sua senha ({repeticoes}): ')

#   if senha_digitada == senha_salva:
#     print('Senha correta!')
#     break

#   repeticoes += 1

# print('O laço acima pode ter infinitas repetições')

texto = 'Python'

novo_texto = ''
for letra in texto:
  novo_texto += f'-{letra}-'

print(novo_texto)
