idade = int(input())        #pede um input e o transforma em inteiro

if idade >=16:              #Condicional principal do código
    print("Pode votar!")    #Impressão da mensagem caso Verdade

else:                       # Aqui o else é obrigatório por não usar o comando *return*
    print("Espere um pouco!")# Impressão da mensagem caso o if seja Mentira(Falso)