"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#   return x + y

def soma(*args): # empacotamento
  total = 0
  for numero in args:
    total += numero
  return total

total_soma = soma(1, 1, 1, 1, 1)
print(total_soma)

numeros = (1, 2, 3, 4, 5, 6, 70, 80, 90)
soma(*numeros) # desempacotamento
print(sum(numeros))
