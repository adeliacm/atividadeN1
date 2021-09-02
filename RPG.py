#joguinho
#arrumar os textos
sala = 1
interacoes = 0
print("bla bla bla do começo\n")
while sala != 9 and interacoes < 7:
  if sala == 6:
    pass #adicionar funções da sala 6
  elif sala == 10:
    pass # adicionar funções para o Portal
  else:
    print("Você está na sala: {}".format(sala))
    caminhoEscolhido = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
    sala = sala + caminhoEscolhido
  interacoes = interacoes + 1
if sala == 9:
  print("você conseguiu!")
else:
  print("f")
