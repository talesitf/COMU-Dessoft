#################################################################################################################################################
                                       #FUNÇÃO#   #FUNÇÃO#  #FUNÇÃO#  #FUNÇÃO#  #FUNÇÃO#
#################################################################################################################################################

# Exercício Segredo do cofre

def calcula_segredo(senha):                     # Define a função
    if int(senha)<100 or int(senha)>999:        # O argumento nesse caso entrava como string em vez de inteiro, teste antes de usar
        return -1                               # Condição de senha com 3 dígitos, existe uma maneira de fazer com lista, voltar depois que tiver a aula
    else:
        num1 = int(senha)%10                    # Função resto "%"
        num2 = int(int(senha)/10)%10            # Aqui o primeiro int funciona como função piso, pense como conversão de um float, tipo: int(4.5) = 4
        num3 = int(int(senha)/100)              #  "        "             "             "         
        return num1+num2+num3

#################################################################################################################################################
#################################################################################################################################################

# Exercício Calcula ângulo de refração
 
import math                                     # Importa math para usar a função seno

def snell_descartes(n1,n2,t1):                  # Define a função com o nome que pedem e argumentos, dessa vez são floats
    teta1_rad=math.radians(t1)                  # Transforma o t1(pode chamar de teta1) em radians
    sen2=math.sin(teta1_rad)*n1/n2              # calcula o seno de teta2 
    res= math.degrees(math.asin(sen2))          # calcula o inverso do seno calculado, e transforma em degraus
    return res

#################################################################################################################################################
#################################################################################################################################################

# Exercício Reflexão interna total

import math                                    # Importa math para usar a função seno

def reflexao_total_interna(n1,n2,t2):          # Define a função com o nome e argumentos pedidos
    
    ang2= math.radians(t2)                     # Transforma t2 em radians
    sen1 = math.sin(ang2)*n2/n1                # calcula o seno do angulo de refração
    
    return sen1 > 1                            # Lembre que condicionais são expressões que têm valor lógico True ou False para o Python, então esse return vai ser exatamente isso, True ou False
                                               # A pegada da questão é saber a física do problema, que n existe sen(w) > 1, mas na conta dá, e esse é justamente o caso de reflexão total.

#################################################################################################################################################
                                               #INPUT#   #INPUT#  #INPUT#  #INPUT#  #INPUT# 
#################################################################################################################################################

# Exercício Redução na vida de um fumante

cig_d=int(input('Quantos cigarros você fuma por dia?'))   # Primeiro input, o texto é pra ajudar a entender a variável
tempo_anos=int(input('E há quantos anos?'))               # Segundo input

num_cig= tempo_anos*365*cig_d                             # Número de cigarros fumados durante esse tempo
tempo_perdido_d = num_cig/6 /24                           # Cálculo que é pedido
print(tempo_perdido_d)                                    # print final

#################################################################################################################################################
                                            #IF#   #IF#   #IF#   #IF#   #IF#   #IF#
#################################################################################################################################################

# Classificador de triângulos

def classifica_triangulo(l1,l2,l3):                      # Define a função com nome e argumentos pedidos
    if l1==l2==l3:                                       # Primeiro caso, com todos os lados iguais
        return "equilátero"
    elif l1==l2 and l1!=l3:                              # Os elifs checam as três possibilidades de ser triângulo isóceles  
        return "isósceles"
    elif l2==l3 and l2!=l1:
        return "isósceles"
    elif l1==l3 and l1!=l2:
        return "isósceles"
    else:                                               # Se não é nem equilátero nem isóceles, é escaleno
        return "escaleno"

#################################################################################################################################################
#################################################################################################################################################

# Exercício Valida Data

def valida_data(d,m,a):                                    # Define a função com o nome e argumentos pedidos
    if d>31 or m>12:                                       # Checa validade inicial da data
        return False
    elif m==2:                                             # Entra no caso de Fevereiro
        if d==29:
            if a%4!=0:                                     # Veja Ano Bissexto
                return False
            elif a%4==0 and a%400==0:
                return True
            elif a%4==0 and a%100==0 and a%400!=0:
                return False
            else:
                return True
        elif d>29:                                        # Data impossível em Fevereiro, que só tem, no máximo 29 dias
            return False
        else:
            return True
    elif m==4 or m==6 or m==9 or m==11 and d==31:         # A função or é associativa, ou seja, pode botar quantas condições você quiser antes do and que o Python entende
        return False
    else:                                                 # Checou todas as possíveis vdatas falsas, então retorna True
        return True

#################################################################################################################################################
#################################################################################################################################################

# Exercício Multa de Velocidade

vel = float(input('Qual a velocidade do carro? '))       # Transforma o input em float
if vel<= 80.0:                                           # Checa se há multa
    print('Não foi multado')
else:
    multa = 5.00*(vel-80.0)                              # Calcula e imprime a multa
    print('{:0.2f}'.format(multa))

#################################################################################################################################################
#################################################################################################################################################

# Exercício Fã de Star Wars

resp2= input("Tem camiseta temática? ")                                    # Todos os inputs devem ser "sim" para a resposta ser considerada positiva
resp1= input("Já assistiu todos os filmes? ")
resp3= input("Já se fantasiou de algum personagem? ")
resp4= input("Tem algum action figure/nave/etc? ")
resp5= input("Já foi no Galaxy's Edge, o parque temático da franquia? ")
soma = 0                                                                  # Apenas um termo para controle de repostas
if resp1 == 'sim':                                                        # os primeiros 5 if´s são idependentes e somam na variável de controle
    soma+=1                                                               # Se a variável não existir, deve-se analisar caso a caso de combinação de resposta
if resp2 == 'sim':
    soma+=1
if resp3 == 'sim':
    soma+=1
if resp4 == 'sim':
    soma+=1
if resp5 == 'sim':
    soma+=1
if soma == 2:                                                             # A partir daqui, se imprime a resposta que se quer, então entra numa estrutura de dependência, para se haver apenas uma resposta 
    print('Padawan')
elif soma == 3 or soma == 4:
    print('Jedi')
elif soma==5:
    print('One with the Force')
else:
    print('Inocente')

#################################################################################################################################################
#################################################################################################################################################

# Exercíco Ano Bissexto

def eh_bissexto(a):                                   # Define a função com nome e argumento pedidos
    if a%4!=0:                                        # Primeiro critério para ano Bissexto
        return False                            
    elif a%4==0 and a%400==0: 
        return True
    elif a%4==0 and a%100==0 and a%400!=0:            # Anos múltiplos de 100, mas não de 400 não são Bissextos (Eu n fiz as regras!!)
        return False
    else:                                             # Não tendo mais casos falsos, retorna verdadeiro
        return True

#################################################################################################################################################
#################################################################################################################################################