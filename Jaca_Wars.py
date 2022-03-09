import math                                 #Importa a biblioteca "math" para usar a função math.sin()

vel = float(input('velocidade: '))          #Primeiro input e conversão para float

teta = float(input('ângulo: '))             #Segundo input e conversão para float

d = math.sin(2*teta*math.pi/180)*vel**2/9.8 #Cálculo da distância que ele pediu. Cheque se o ângulo veio em grau ou radiano e faça a conversão se necessário

if d <102 and d > 98:                       #Condicional de Intervalo:  A < X **and** X < B,
    print('Acertou!')                       #imprime o texto

elif d<=98:                                 #Sedunda condicional, caso a primeira falhe:
    print('Muito perto')                    #imprime o texto

else:                                       #else que poderia ser (elif d>=102:) mas aumenta a complexidade do programa
    print('Muito longe')                    #imprime o texto


