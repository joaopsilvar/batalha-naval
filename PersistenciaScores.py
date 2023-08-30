class PersistenciaScores:
  def __init__(self):
    pass

  def registrarPontuacao(self,nome,contagem):
    with open('scores.txt','a+') as arquivo:
      arquivo.seek(0)  # Reposiciona o ponteiro de leitura no início do arquivo
      linhas = arquivo.readlines()
   
      if linhas:
        ultima_linha = linhas[-1]
        ultima_linha = ultima_linha.split()[0].strip()
        indice = int(ultima_linha) + 1
      else:
        arquivo.write(f"{'Número':<12}{'Nome':<15}{'Quantidade de Jogadas':<21}\n")
        indice = 1

      arquivo.write(f'{indice:<12}{nome:<15}{contagem:<21}\n')
    self.ordenarPontuacao('scores.txt')
      
  def ordenarPontuacao(self,caminho_arquivo):
    pontuacoes = []
    # Lê as pontuações existentes do arquivo
    with open(caminho_arquivo, 'r') as arquivo:
      linhas = arquivo.readlines() 
      for linha in linhas[1:]:  # Ignora o cabeçalho
        nome = linha[12:27].strip()
        contagem = int(linha[27:].strip())
        pontuacoes.append((contagem,nome)) 
    
    # Ordena as pontuações com base na contagem de jogadas
    pontuacoes = sorted(pontuacoes, key=lambda x: x[0])
    
    # Reescreve as pontuações ordenadas da menor quantidade de jogadas para maior
    with open(caminho_arquivo, 'w') as arquivo:
      if linhas:
        arquivo.write(f"{'Número':<12}{'Nome':<15}{'Quantidade de Jogadas':<21}\n")      # Escreve o cabeçalho novamente
      contador = 0
      for linha in pontuacoes:
        contador+=1
        arquivo.write(f'{contador:<12}{linha[1]:<15}{linha[0]:<21}\n')