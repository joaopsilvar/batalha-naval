class Exibicao:

  def __init__(self):
    self.contador_jogadas = 0
    self.navios_encontrados = 0
    self.submarinos_encontrados = 0

  def setContadorJogadas(self):
    self.contador_jogadas += 1

  def setNaviosEncontrados(self):
    self.navios_encontrados += 1

  def setSubmarinosEncontrados(self):
    self.submarinos_encontrados += 1

  def imprimirDadosJogo(self, tabuleiro):
    print(f'\nJogadas até o momento: {self.contador_jogadas}')
    print('Afundados:')
    print(f'\u26F5 Navios: {self.navios_encontrados} de {tabuleiro.navios}')
    print(
      f'\U0001F6A2 Submarinos: {self.submarinos_encontrados} de {tabuleiro.submarinos}'
    )

  def imprimirTabuleiro(self, tabuleiro):
    print('    ', end='')
    for col in tabuleiro.colunas:
      print(f'{col:2}', end='')
    print()

    for l in range(len(tabuleiro.linhas)):
      print(f'{tabuleiro.linhas[l]} |  ', end='')
      for c in range(len(tabuleiro.colunas)):
        print(f'{tabuleiro.tabuleiro[l][c]:2}', end='')
      print()

  def imprimirPontuacoes(self):
    with open('scores.txt', 'r') as arquivo:
      linhas = arquivo.readlines()
      print('\n        ===== MELHORES PONTUAÇÕES =====         ')
      for linha in linhas:
        print(linha, end='')