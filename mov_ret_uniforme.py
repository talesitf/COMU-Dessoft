def calcula_posicao(t,s0,v): #Cria a função com nome e argumento *na ordem* que vão ser utilizados
    
    pos = v*t + s0           #Cria uma variável com o cálculo pedido
    return pos               #Retorna o valor calculado na variável

# A seguinte notação também é possível, use a que fizer mais sentido para você:
# 
## def calcula_posicao(t,s0,v):
##    
##     return (v*t + s0)    Aqui o cálculo é feito direto no return  