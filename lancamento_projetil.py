import math                                   #Importa a biblioteca math para ter acesso às funções trigonométricas

def calcula_distancia_do_projetil(v,teta,yo): #Se define a função com o nome e argumentos **na ordem que vão ser usados**.
    
    #Separe em argumentos a resposta, para poder visualizar melhor seu código
    arg_1 = (v**2)/(2*9.8)                      #primeira expressão da resposta 
    
    arg_2 = 2*9.8*yo/((v**2)*(math.sin(teta)**2)) #Aqui, teste se o argumento teta vai ser dado em graus ou radianos
                                                  #Note também que arg_2 = 2*(math.sin(teta)**2)/arg_1
    
    d = arg_1 * (1+ math.sqrt(1+arg_2))*math.sin(2*teta) #Junta os argumentos na forma que ele quer a resposta. Usa a função math.sqrt() que devolve a raiz quadrada
    
    return d                                      #retorna a resposta final calculada.