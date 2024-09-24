# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# não é recomendavel converter os valores direto na variável que recebe o valor
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# criando variáveis com o único objetivo de converter os valores de numero_1 e numero_2 para int
int_numero_1 = int(numero_1)  
int_numero_2 = int(numero_2) 

soma = int_numero_1 + int_numero_2

print(f'A soma dos números é: {soma}')
