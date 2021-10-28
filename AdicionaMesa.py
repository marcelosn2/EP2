def adiciona_na_mesa(peca, mesa):
    if len(mesa)!=0:
        num_mesa1 = mesa[0][0]
        num_mesa2 = mesa[-1][1]

        num_peca1 = peca[0]
        num_peca2 =peca[1]
        
        if num_peca2==num_mesa1:
            mesa.insert(0,peca)
            return (mesa)
        elif num_peca1==num_mesa1:
            peca.reverse()
            mesa.insert(0,peca)
            return (mesa)
        elif num_peca1==num_mesa2:
            mesa.append(peca)
            return (mesa)
        elif num_peca2==num_mesa2:
            peca.reverse()
            mesa.append(peca)
            return (mesa)    
    else:
        mesa.append(peca)
        return(mesa)