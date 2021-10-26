from CriaPecas import cria_pecas
def inicia_jogo(num,pecas):
    i = 1
    jogo={}
    jogadores ={}
    while i <= num:
        jogadores[i-1] = pecas[:7]
        del pecas[:7]
        i +=1
    jogo['jogadores'] = jogadores

    jogo['monte']=pecas
    jogo['mesa']=[]



    return (jogo)

