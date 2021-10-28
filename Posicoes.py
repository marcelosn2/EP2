def posicoes_possiveis(mesa,pecas):
    index = 0
    posicoes = []
    if len(mesa)!=0:
        num1=mesa[0][0]
        num2=mesa[-1][1]
    else:
        return([0,1,2,3,4,5,6])

    for p in pecas:
        for i in p:
            if i == num1 or i == num2:
                posicoes.append(index)
        index+=1
    posicoes = list(set(posicoes))
    return(posicoes)