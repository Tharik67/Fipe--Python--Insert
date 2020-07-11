# gerar cpf valido aleatorio com o estado dele
# pegar nomes inseridos no txt
# pegar sobrenomes inseridos no txt
# gerar uma data aleatoria de 18 a 85 anos
# salvar em um txt: 
# insert into consumidores values (CPF, Nome, Sobrenome,Data_nascimento,Estado) 
# funcao que retorna um cpf ja salvo


import random 
import math

import datetime

def gera_data(comeco , fim):
    date=datetime.date(random.randint(comeco , fim), random.randint(1,12),random.randint(1,28))
    return date

def gera_cpf():                                                                                                    
    n = [random.randrange(10) for i in range(9)]
                                                                                                    
    # calcula digito 1 e acrescenta ao numero
    s = sum(x * y for x, y in zip(n, range(10, 1, -1)))
    d1 = 11 - s % 11
    if d1 >= 10:
        d1 = 0
    n.append(d1)
                                                                                                    
    # calcula digito 2 e acrescenta ao numero
    s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
    d2 = 11 - s % 11
    if d2 >= 10:
        d2 = 0
    n.append(d2)
                                                                                                    
    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)

def gera_estado(cpf):
    n= int(cpf[11])
    if n == 1 :
        estado = ['DF','GO','MT','MS','TO']
    elif n == 2:
        estado = ['PA','AM','RR','RO','AC','AP']
    elif n == 3:
        estado = ['MA','CE','PI']
    elif n == 4:
        estado = ['PB','PE','AL','RN']
    elif n == 5:
        estado = ['BA','SE']
    elif n == 6:
        estado = ['MG']
    elif n == 7:
        estado = ['RJ','ES']
    elif n == 8:
        estado = ['SP']
    elif n == 9:
        estado = ['PR','SC']
    else:
        estado=['RS']
        
    return random.choice(estado)
        
def gera_nome (nome):
    nome = random.choice(nomes)
    return nome



saida_consumidor = open('consumidores.txt','w')
saida_cpf = open('cpf.txt','w')
arq_nomes = open("nomes.txt" , "r")
arq_sobrenomes = open("sobrenomes.txt" , "r")

nomes = []
for linha in arq_nomes:
    linha.strip()
    nomes.append(linha[:-2])
        
sobrenomes = []
for linha in arq_sobrenomes:
    linha.strip()
    nomes.append(linha[:-2])      

def gera_consumidor(saida_consumidor,saida_cpf,nomes,sobrenome):
    cpf = gera_cpf()
    nome = gera_nome(nomes)
    sobrenome = gera_nome(sobrenome)
    estado = gera_estado(cpf)
    data = gera_data(1940,2002)
    txt = "('%s', '%s', '%s', '%s', '%s')\n" %(cpf, nome, sobrenome,data,estado)
    txt2 = "%s\n" %cpf
    saida_consumidor.write(txt)
    saida_cpf.write(txt2)
    

for i in range(3000):
    gera_consumidor(saida_consumidor,saida_cpf,nomes,sobrenomes)


arq_nomes.close()
arq_sobrenomes.close()