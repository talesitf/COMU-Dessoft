def pedra_papel_tesoura(j1,j2):                                 #Define a função e os argumentos usados de forma entendível(seja claro de forma a enteder j1 --> jogador1, e j2 --> jogador2)
    
    
    if j1 != "papel" and j1 != "tesoura" and j1 != "pedra":     #Condicional caso o j1 n tenha jogado certo
        return "Escolha pedra, papel ou tesoura para jogar"
    
    
    elif j2 != "papel" and j2 != "tesoura" and j2 != "pedra":   #Condicional caso o j2 n tenha jogado certo
        return "Escolha pedra, papel ou tesoura para jogar"
    
    
    elif j1 == "papel":                                         #Casos caso o jogador 1 tenha jogado papel
        
        if j2 == "papel":
            return "empate"
        elif j2 == "tesoura":
            return "dois"

        return "um"                                             #Tanto esse como nos outros casos, esse último return pode vir dentro de um else, faça de forma a entender melhor o código.
    
    
    elif j1 == "tesoura":                                       #Casos caso o jogador 1 tenha jogado tesoura
        
        if j2 == "papel":
            return "um"
        elif j2 == "tesoura":
            return "empate"
        
        return "dois"
    
    
    elif j1 == "pedra":                                         #Casos caso o jogador 1 tenha jogado pedra
        
        if j2 == "pedra":
            return "empate"
        elif j2 == "tesoura":
            return "um"
        
        return "dois"