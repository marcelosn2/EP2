from InicioJogo import inicia_jogo 
from CriaPecas import cria_pecas

def verifica_ganhador(jogadores):
    i=1
    while i <= (len(jogadores.keys())):
        print(len(jogadores.keys()))
        if len(jogadores[i-1])==0:
            return(i)
        else:
            i+=1 
    print('saiu')
    return(-1)


x = inicia_jogo(3,cria_pecas())
xx = x["jogadores"]
print(verifica_ganhador(xx))
#print(len(xx[0]))
