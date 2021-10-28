from AdicionaMesa import adiciona_na_mesa
from CriaPecas import cria_pecas
from InicioJogo import inicia_jogo
from VerificaGanhador import verifica_ganhador
from Posicoes import posicoes_possiveis
from AdicionaMesa import adiciona_na_mesa
from SomaPontos import soma_pecas


jogadores=int(input('Quantos jogadores?: '))
pecas=cria_pecas()
Jogo=inicia_jogo(jogadores,pecas)
print(Jogo)
print("VEZ DO JOGADOR 1")
print ("JOGADAS POSSIVEIS {0}".format(posicoes_possiveis(Jogo['mesa'], Jogo["jogadores"][0])))
escolida=int(input('escolha uma peça: '))
adiciona_na_mesa(Jogo['jogadores'][0][escolida],Jogo['mesa'])


print(Jogo)