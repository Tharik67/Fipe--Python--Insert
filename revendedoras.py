# gerar CNPJ valido aleatorio 
# pegar nomes inseridos no revendedora.txt
# estado aleatorio
# salvar em um txt: 
# insert into consumidores values (CNPJ, Nome, CPFproprietario, Estado) 
# funcao que retorna CNPJ aleatorio de alguma revendedora

import random

def cnpj(punctuation = True):
    n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
    v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
    # calcula dígito 1 e acrescenta ao total
    s = sum(x * y for x, y in zip(reversed(n), v))
    d1 = 11 - s % 11
    if d1 >= 10:
      d1 = 0
    n.append(d1)
    # idem para o dígito 2
    s = sum(x * y for x, y in zip(reversed(n), v))
    d2 = 11 - s % 11
    if d2 >= 10:
      d2 = 0
    n.append(d2)
    if punctuation:
      return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
    else:
      return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)
  
def gera_estado():
    estado = ['DF','GO','MT','MS','TO''PA','AM','RR','RO','AC','AP','MA','CE','PI','PB','PE','AL','RN','BA','SE','MG','RJ','ES','SP','PR','SC','RS']
    return random.choice(estado)

def getCPF(nome):
    nome = random.choice(nomes)
    return nome
    

def getname(nome):
    nome = random.choice(nomes)
    return nome
    
arq_nomes = open("nomes_reve.txt",'r') 
nomes = []
for linha in arq_nomes:
    linha.strip()
    nomes.append(linha[:-2])   
    
arq_cpf = open("cpf.txt",'r') 
cpfs = []
for linha in arq_cpf:
    linha.strip()
    cpfs.append(linha[:-2])  
    

saida_revendedora = open("revendedora.txt" , "w")
saida_cnpj = open("cnpj.txt",'w')
def gera_revendedora (saida_revendedora,saida_cnpj,n):
    CNPJ = cnpj()
    Nome = n
    CPFproprietario = getCPF(cpfs)
    Estado = gera_estado()

    txt1 = "Insert into revendedoras ('%s', '%s', '%s', '%s');\n" %(CNPJ, Nome, CPFproprietario, Estado)
    txt2 = "%s\n" %CNPJ
    
    saida_revendedora.write(txt1)
    saida_cnpj.write(txt2)
    
    
for n in range(len(nomes)):
    gera_revendedora(saida_revendedora,saida_cnpj,n)
    
    
saida_revendedora.close()
saida_cnpj.close()
arq_cpf.close()
arq_nomes.close()