from AdicionaMesa import adiciona_na_mesa
from CriaPecas import cria_pecas
from InicioJogo import inicia_jogo
from VerificaGanhador import verifica_ganhador
from Posicoes import posicoes_possiveis
from SomaPontos import soma_pecas


jogadores=int(input('Quantos jogadores?: '))
pecas=cria_pecas()
Jogo=inicia_jogo(jogadores,pecas)
print(Jogo)

JOGO = -1
numero=0

while JOGO == -1:
    print("VEZ DO JOGADOR {0} ".format(numero+1))
    print('MESA: {0}'.format(Jogo['mesa']))
    print('SUA MÃO: {0}'.format(Jogo["jogadores"][numero]))
    print ("JOGADAS POSSIVEIS {0}".format(posicoes_possiveis(Jogo['mesa'], Jogo["jogadores"][numero])))

    if len(posicoes_possiveis(Jogo['mesa'], Jogo["jogadores"][numero])) == 0:
        print('Sem jogadas possiveis, compre do monte')
        if len (Jogo['monte']) != 0:
            Jogo['jogadores'][numero].append(Jogo['monte'][0])
            del Jogo['monte'][0]
        else:
            print ('Não ha cartas no monte')
    else:
        escolida=int(input('escolha uma peça: '))
        adiciona_na_mesa(Jogo['jogadores'][numero][escolida],Jogo['mesa'])
        del Jogo['jogadores'][numero][escolida]
        print(Jogo['mesa'])
    JOGO = (verifica_ganhador(Jogo['jogadores']))
    if JOGO == (-1):
        print ('============================================================================')
        if (numero+1) < jogadores:
            numero += 1
        else :
            numero = 0
        JOGO = -1
    else:
        print('ganhador'+0)
        JOGO = 1

print ('finalizado')