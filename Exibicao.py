from Tabuleiro import Tabuleiro

class Exibicao:
  def __init__(self):
    self.contador_jogadas = 0
    self.navios_encontrados = 0
    self.submarinos_encontrados = 0

  def getContadorJogadas(self):
    return self.contador_jogadas

  def setContadorJogadas(self):
    self.contador_jogadas += 1
        
  def getNaviosEncontrados(self):
    return self.navios_encontrados

  def setNaviosEncontrados(self):
    self.navios_encontrados += 1
    
  def getSubmarinosEcontrados(self):
    return self.submarinos_encontrados

  def setSubmarinosEncontrados(self):
    self.submarinos_encontrados += 1

  def getNaviosSubmarinosEncontrados(self):
    return self.navios_encontrados + self.submarinos_encontrados
    
  def imprimirDadosJogo(self,tabuleiro):
    print(f'\nJogadas até o momento: {self.contador_jogadas}')
    print('Afundados:')
    print(f'\u26F5 Navios: {self.navios_encontrados} de {tabuleiro.getNaviosTabuleiro()}')
    print(f'\U0001F6A2 Submarinos: {self.submarinos_encontrados} de {tabuleiro.getSubmarinosTabuleiro()}')
  
  def imprimirTabuleiro(self,tabuleiro): 
    print('    ',end = '')
    for col in tabuleiro.getColunasTabuleiro():
      print(f'{col:2}',end = '')
    print()

    for l in range(len(tabuleiro.getLinhasTabuleiro())):
      print(f'{tabuleiro.getLinhasTabuleiro()[l]} |  ',end = '')
      for c in range(len(tabuleiro.getColunasTabuleiro())):
        print(f'{tabuleiro.getTabuleiro()[l][c]:2}',end = '')
      print()

  def imprimirPontuacoes(self):
    with open('scores.txt','r') as arquivo:
      linhas = arquivo.readlines()
      print('\n        ===== MELHORES PONTUAÇÕES =====         ')
      for linha in linhas:
        print(linha,end = '')
  