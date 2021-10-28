def verifica_ganhador(jogadores):
    i=1
    while i <= (len(jogadores.keys())):
        if len(jogadores[i-1])==0:
            return(i-1)
        else:
            i+=1 
    return(-1)
