# def duplicar(numero):
#   return numero * 2

# def triplicar(numero):
#   return numero * 3

# def quadruplicar(numero):
#   return numero * 4

def criar_multiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)
