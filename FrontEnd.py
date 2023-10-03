from PersistenciaScores import PersistenciaScores
from Tabuleiro import Tabuleiro
from Exibicao import Exibicao

class FrontEnd:
  def __init__(self):
    pass

  def startGame(self):
    opcao = 0
    while opcao != 3:
      print(f'\n\u26F5\u26F5\u26F5 Batalha Naval \u26F5\u26F5\u26F5\n')
      print(f'1 - Jogar\n2 - Ver Melhores Pontuações\n3 - Sair')
      opcao = eval(input('Escolha uma opção:'))
      if opcao == 1:
        print(opcao)
        tabuleiro = Tabuleiro() #objeto inicializado
        tabuleiro.gerarNovoTabuleiro() #tabuleiro criado
        
        exibicao = Exibicao()#objeto inicializado
        exibicao.imprimirTabuleiro(tabuleiro)#imprime o tabuleiro
        exibicao.imprimirDadosJogo(tabuleiro)#imprime os dados do jogo
      
        while True:
          try:
            selecao = eval(input(f'\nDigite a posição para tentar (formato linha,coluna)\nSe quiser desistir digite -1: '))
          except:
            print('Entrada Inválida:')
            continue
          if selecao == -1:
            print('Jogador Desistiu')
            break
          elif type(selecao) != tuple or len(selecao) != 2:
            print('Entrada Inválida')
          elif len(selecao) == 2 and (type(selecao[0]) != str or type(selecao[1]) != int):
            print('Entrada Inválida')
          else:
            print('Efetuando a jogada....')
            resultado = tabuleiro.efetuarJogada(selecao)
            exibicao.setContadorJogadas()
            if resultado == 0:
              print('Submarino Parcialmente Atingido')
            elif resultado == 1:
              print('Submarino Afundado')
              exibicao.setSubmarinosEncontrados()
            elif resultado == 2:
              print('Navio Afundado')
              exibicao.setNaviosEncontrados()
            else:
              print('Agua Encontrada')
          
            exibicao.imprimirTabuleiro(tabuleiro)
            exibicao.imprimirDadosJogo(tabuleiro)

            count = exibicao.navios_encontrados + exibicao.submarinos_encontrados
            if count == tabuleiro.navios + tabuleiro.submarinos:
              print('\n\u002A\u002A\u002A\u002A\u002A Parabéns! Você Ganhou!!!!! \u002A\u002A\u002A\u002A\u002A\n')
              nome_ganhador = input('Informe seu nome:')
              contador_jogadas = exibicao.contador_jogadas
              score = PersistenciaScores()
              score.registrarPontuacao(nome_ganhador,contador_jogadas)
              exibicao.imprimirPontuacoes()
              break

      elif opcao == 2:
        exibicao = Exibicao()
        exibicao.imprimirPontuacoes()
    
      elif opcao == 3:
        opcao = 3