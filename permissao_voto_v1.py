def idade_votacao(idade):       #define uma função que retorna o texto a ser impresso, seja claro no nome e argumento dela
    
    if idade>=16:               # condicional principal do código
        return "Pode votar!"    # Texto caso verdade
   #else:                           # O else pode ser usado, mas n pe necessário, faça como preferir, o (elif idade <16:) pode ser considerado complexidade
   #    return "Espere um pouco!"
    return "Espere um pouco!"   #Texto caso mentira

    

idade = int(input())            # O input que ele pede
print(idade_votacao(idade))     # Print do texto dado pela função a partir do input