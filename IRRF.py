sal_b = float(input('salário bruto: '))             #pede o input do salário bruto e converte para float. Use o nome que fizer sentido para você

num_d = float(input('Npumero de dependentes: '))    #pede o input do número de dependentes. Use o nome que fizer sentido para você

cont_INSS = 0                                       #define uma variável para "contribuição para o INSS", para manipular depois
ali = 0                                             #define uma variável para alíquota
ded = 0                                             #define uma variável para a dedução

if sal_b <= 1045:                                   #Série de condicionais para definir a contribuição de acordo com a tabela dada
    cont_INSS = 0.075*sal_b
elif sal_b > 1045 and sal_b <= 2089.60:
    cont_INSS = 0.09*sal_b
elif sal_b > 2089.60 and sal_b <= 3134.40:
    cont_INSS = 0.12*sal_b
elif sal_b > 3134.40 and sal_b <= 6101.06:
    cont_INSS = 0.14*sal_b
else :
    cont_INSS = 671.12

base = sal_b - cont_INSS - num_d*189.59             #Cálculo da base de cálculo do jeito pedido

if base <= 1903.98:                                 #Série de condicionais para definir a alíquota e a dedução
    ali = 0
    ded = 0
elif base <= 2826.65:
    ali = 0.075
    ded = 142.80 
elif base <= 3751.05:
    ali = 0.15
    ded = 354.80
elif base <= 4664.68:
    ali = 0.225
    ded = 636.13
else :
    ali = 0.275
    ded = 869.36

irrf = base*ali-ded                                 #Por fim, o cálculo do IRRF

print(irrf)                                         #Print do IRRF