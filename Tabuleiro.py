import random
class Tabuleiro:
  def __init__(self):
    #atributos de configuração do jogo
    self.linhas = ['A','B','C','D','E','F']
    self.colunas = [1,2,3,4,5,6]
    self.navios = 5
    self.submarinos = 3

    #atributos para geração do tabuleiro e sorteio das posições
    self.posicao_navios = {}
    self.posicao_submarinos = {}
    self.tabuleiro = []

    #atributo para controle das jogadas
    self.submarinos_eliminados = {}
    self.submarinos_parcialmente_atingido = {}
    self.navios_eliminados = {}

  def getLinhasTabuleiro(self):
    return self.linhas

  def getColunasTabuleiro(self):
    return self.colunas

  def getNaviosTabuleiro(self):
    return self.navios

  def getSubmarinosTabuleiro(self):
    return self.submarinos  
  
  def getPosicaoNavios(self):
    return self.posicao_navios

  def getPosicaoSubmarinos(self):
    return self.posicao_submarinos

  def getTabuleiro(self):
    return self.tabuleiro

  def getQtdeNaviosSubmarinos(self):
    return self.navios + self.submarinos
  
  def gerarPosicoesSubmarinos(self):
    for i in range(self.submarinos):
      while True:
        #sortea posição 1 do submarino , valida se não está ocupado a posição e cria uma lista de adjacentes
        s1_linha = random.choice(self.linhas)
        s1_coluna = random.choice(self.colunas)
        p1 = (s1_linha,s1_coluna)
      
        if all(p1 != posicao for posicoes in self.posicao_submarinos.values() for posicao in posicoes):  
          iLinha = self.linhas.index(s1_linha)
          iColuna = self.colunas.index(s1_coluna)
          
          adjacentes = []

          if iLinha < len(self.linhas)-1:
            adjacentes.append((self.linhas[iLinha+1], self.colunas[iColuna]))
          if iLinha > 0:
            adjacentes.append((self.linhas[iLinha-1], self.colunas[iColuna]))
          if iColuna < len(self.colunas)-1:
            adjacentes.append((self.linhas[iLinha], self.colunas[iColuna+1]))
          if iColuna > 0:
            adjacentes.append((self.linhas[iLinha], self.colunas[iColuna-1]))

          #sortear a posição 2 da lista de adjacentes da posição 1 do submarino e valida se a posição não está ocupada e inclui as posições dentro da lista de posições do submarino
          while adjacentes:
            p2 = random.choice(adjacentes)
            if all(p2 != posicao for posicoes in self.posicao_submarinos.values() for posicao in posicoes):
              self.posicao_submarinos[f'sub{i}'] = (p1,p2)
              break
            else:
              adjacentes.remove(p2)   
          break

  def gerarPosicoesNavios(self):
    for i in range(self.navios):
      
      navios_submarinos = {}
      for d in [self.posicao_submarinos, self.posicao_navios]:
        navios_submarinos.update(d) 
      while True:
        
        n_linha = random.choice(self.linhas)
        n_coluna = random.choice(self.colunas)
        n = (n_linha,n_coluna)

        if all(n != posicao for posicoes in navios_submarinos.values() for posicao in posicoes):  
          self.posicao_navios[f'nav{i}'] = n
          break

  def gerarNovoTabuleiro(self):    
    #faz a criação do novo tabuleiro com as peças padrão
    for linha in self.linhas:
      li = []
      for coluna in self.colunas:
        li.append('\u2585')
      self.tabuleiro.append(li)
    
    self.gerarPosicoesSubmarinos() #gera as posições aleatorias dos submarinos. É importante que os submarinos sejam gerados antes dos navios.
    self.gerarPosicoesNavios() #gera as posições aleatorias dos navios

  def atualizarTabuleiroJogada(self,entrada,caracter):
    for indexL,linha in enumerate(self.linhas):
      for indexC,coluna in enumerate(self.colunas):
        if entrada[0] == linha and entrada[1] == coluna:
          self.tabuleiro[indexL][indexC] = caracter
        
  def efetuarJogada(self,entrada):
    #valida a entrada informada é de um submarino ainda não atingido e move para parcialmente atingido
    for sub,posicoes in self.posicao_submarinos.items():
      for posicao in posicoes:
        if entrada == posicao:
          self.atualizarTabuleiroJogada(entrada,'\u2316') #atualizar tabuleiro com o caracter parcialmente atingido
          self.submarinos_parcialmente_atingido[sub] = posicoes #copia submarino para parcialmente atingido
          del self.posicao_submarinos[sub] #remove submarido de posicao submarino
          return 0 #0 = submarino parcialmente atingido

    #valida se a entrada é um submarino particalmente atingido e move para eliminado
    for sub,posicoes in self.submarinos_parcialmente_atingido.items():
      for posicao in posicoes:
        if entrada == posicao:
          self.atualizarTabuleiroJogada(posicoes[0],'X') #atualiza a posicao 0 do submarino para eliminado
          self.atualizarTabuleiroJogada(posicoes[1],'X') #atualiza a posicao 1 do submarino para eliminado
          self.submarinos_eliminados[sub] = posicoes #copia submarino para a lista de eliminados
          del self.submarinos_parcialmente_atingido[sub] # remove submarino de parcialmente atingidos
          return 1 #1 = submarino afundado

    #valida se a entrada é um navio e move para eliminado
    for nav,posicao in self.posicao_navios.items():
      if entrada == posicao:
        self.atualizarTabuleiroJogada(entrada,'X')
        self.navios_eliminados[nav] = posicao #copia o navio para a lista de eliminados
        del self.posicao_navios[nav] #remove o navio das posicoes do navio
        return 2 #2 = navio afundado

    #executa caso nao ecnontre nenhum submarino ou navio, ou seja foi encontrado agua
    self.atualizarTabuleiroJogada(entrada,'_')
    return 3 #3 = agua encontrada