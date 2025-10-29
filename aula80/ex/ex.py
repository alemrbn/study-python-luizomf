class Pergunta():
  perguntas = [
  {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4'
  },
  {
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25'
  },
  {
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5'
  }
]

  def __init__(self):
    self.start()
  
  def start(self):
    acertos = 0
    for dicionario in self.perguntas:
      print('Pergunta:', dicionario['Pergunta'])
      print()

      opcoes = dicionario['Opções']
      for index, valor in enumerate(opcoes):
        print(f'{index})', valor)
        
      print()
      
      resposta_usuario = input('Digite sua resposta: ')
      resposta_usuario_int = None
      acertou = False
      qtd_opcoes = len(opcoes)
      if resposta_usuario.isdigit():
        resposta_usuario_int = int(resposta_usuario)
      
      if resposta_usuario_int is not None:
        if resposta_usuario_int >= 0 and resposta_usuario_int < qtd_opcoes:
          if opcoes[resposta_usuario_int] == dicionario['Resposta']:
            acertou = True

      if acertou:
        print('Você acertou!')
        print()
        acertos += 1
      else:
        print('Você errou!')
        print()
      
    print('Quantidade de acertos:', acertos, 'de', len(dicionario))
        
