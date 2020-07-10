# pegar CNPJrevenda da funcao de revendedoras
# pegar codigoAuto e ano de automoveis.txt
# insert into negocios values (CNPJrevenda, CodigoAuto, AnoAuto, Quantidade)

import random



def get_carro():
    arq_auto = open("automoveis.txt",'r')
    i = random.randint(1,1042)
    for el in arq_auto:
        i-=1
        if i == 0:
            a =el.split(',')
            b= a[0][3:-1]
            c= int(a[3])
            arq_auto.close()
            return (b,c)
        



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
    
saida_garagem = open("garagem.txt" , 'w')
for CNPJ in cnpjs:
    
    ncar = random.randint(1,7)
    carros = get_listcarro(ncar )
    print(carros)
    for carro in carros:
        quantidade = random.randint(1,10)
        try:
            ano = int(carro[1])
            txt = "('%s' , '%s' , %d , %d) \n" %(CNPJ , carro[0] ,ano , quantidade)
            saida_garagem.write(txt)
        except :
            pass            
  

