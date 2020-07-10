# pegar CNPJrevenda da funcao de revendedoras
# gerar data aleatorio desde 2010
# pegar codigoAuto e ano de automoveis.txt
# gerar preco com variacao de 10% do automoveis.txt
# pegar CPF da funcao de consumidores
# insert into garagens values  (CPFcomprador, CNPJrevenda, CodigoAuto, AnoAuto, Data, Preço)

import random 
import math

import datetime


def gera_data(comeco , fim):
    #date=datetime.datetime(random.randint(comeco , fim), random.randint(1,12),random.randint(1,28),random.randint(0,20), random.randint(0,59), random.randint(0,59))
    date=datetime.date(random.randint(comeco , fim), random.randint(1,12),random.randint(1,28))
    return date



def get_carro():
    arq_auto = open("automoveis.txt",'r')
    i = random.randint(1,1042)
    for el in arq_auto:
        i-=1
        if i == 0:
            a =el.split(',')
            b= a[0][2:-1]
            c= int(a[3])
            d = int(a[5][:-3])
            arq_auto.close()
            return (b,c,d)
        




def get_listcarro(ncar ):
    
    i=[]
    for n in range(ncar):
        flag=0
        carro = get_carro()
        for el in i:
            if carro == el:
                flag = 1
        if flag == 0:
            i.append(carro)
        if None in i:
            i = i[:-1]
    return i
    

arq_cnpj = open('cnpj.txt' , 'r')
cnpjs = []
for linha in arq_cnpj:
    linha.strip()
    cnpjs.append(linha[:-1])
    
arq_cpf = open('cpf.txt','r')
cpfs = []
for linha in arq_cpf:
    linha.strip()
    cpfs.append(linha[:-1])

saida_negocios = open("negocios.txt" , "w")  
#saida_garagem = open("garagem.txt" , 'w')
for CPF in cpfs:    
    ncar = random.randint(1,2)
    k = random.randint(1,3)
    revendas = random.choices(cnpjs , k=k)
    carros = get_listcarro(ncar)
    for carro in carros:
        cnpj = random.choice(revendas)
        codigo = carro[0]
        ano = carro[1]
        data = gera_data(carro[1] , 2020)
        variacao = random.randint(1,3)*10
        preco = carro[2] *variacao

        txt = "('%s' , '%s','%s' , %d ,'%s' , %d) \n" %(CPF , cnpj,codigo ,ano , data, preco)
        saida_negocios.write(txt)
    
    #(CPFcomprador, CNPJrevenda, CodigoAuto, AnoAuto, Data, Preço)  
    
saida_negocios.close()
arq_cnpj.close()
arq_cpf.close()
