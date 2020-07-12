#cria txt com codigo sql para insercao de carros com ano acima de 2010
#
#Atencao :
#A api bloqueia muitas consultas por minuto
#Assim foi inserido tempo de espera a cada consulta
#Por isso codigo pode demorar muito tempo
#Recomendasse fazer pesquisas menores como buscar uma marca de cada vez



import time
import json, requests


save = open('cont.txt' , 'w')
saida = open('automoveis.txt', 'w')

def escolha (marcas):
    i=0
    lista = []
    for el in marcas:
        print ('%d   -  %s' %(i , el['name']))
        i+=1
    
    print("escolha a marca que deseja buscar")
    print("-1 para finalizar")
    while True:
        
        a =int(input())
        if a  < 0:
            break
        else:
            if marcas[a] in lista:
                pass
            else:
                lista.append(marcas[a])
            
        print(lista)
    return lista

#busca o pais da marca, no txt marcaAutomovies
#caso nao ache, pede ao usuario 
def get_pais(marca):
    arquivo = open('marcaAutomoveis.txt','r+')
    marca = marca.upper()
    for linha in arquivo:
        i = linha.index(":")
        if marca in linha[:i]: 
            i+=1
            arquivo.close()
            return(linha[i:])
        
    print("!nao achei %s no arquivo!" %marca)
    pais = input("qual o pais de fabricacao da marca %s :" %marca)
    dic = '\n%s:%s' %(marca,pais)
    arquivo.write(dic)
    return pais 
    
    
#tipos_automoveis= ['motos' , 'carros' , 'caminhoes']
tipos_automoveis= ['carros']


i=0

for tipo in tipos_automoveis:
    
    #A tabela Fipe bloqueia muitas pesquisas
    #por isso a cada vez que utilizamos, o programa espera 1 segundo para continuar
    time.sleep(1)
    html_marca = "http://fipeapi.appspot.com/api/1/%s/marcas.json" %tipo

    api_marca = requests.get(html_marca)
    json_marca = json.loads(api_marca.content)
    #lista = escolha(json_marca)
    lista = json_marca
    
    
    for marca in lista[1:]:
        
        id_marca = marca['id']
        time.sleep(1)
        html_veiculo = "http://fipeapi.appspot.com/api/1/%s/veiculos/%d.json" %(tipo,id_marca)
        api_veiculo = requests.get(html_veiculo)
        json_veiculo = json.loads(api_veiculo.content)
        
        for veiculo in json_veiculo:

            id_veiculo = veiculo['id']
            time.sleep(1)
            html_automovel = "http://fipeapi.appspot.com/api/1/%s/veiculo/%d/%s.json" %(tipo,id_marca,id_veiculo)
            api_automovel = requests.get(html_automovel)
            json_automovel = json.loads(api_automovel.content)
            
            for el in json_automovel:
            
                print("Rodando ... Inseridos:" ,i)              
                ano_veiculo = el['id']

                if int(ano_veiculo[:-2]) < 2010 or int(ano_veiculo[:-2]) > 2021:
                    break
                            
                time.sleep(1)
                html_ano = "http://fipeapi.appspot.com/api/1/%s/veiculo/%d/%s/%s.json" %(tipo,id_marca,id_veiculo,ano_veiculo)
                api_ano = requests.get(html_ano)
                
                automovel = json.loads(api_ano.content)
                pais = get_pais(automovel['marca'])
                codigo =automovel['fipe_codigo']
                fabricante = automovel['marca']
                modelo = automovel['veiculo']
                ano = int(automovel['ano_modelo'])
                preco = automovel['preco'][3:-3]
                preco = preco.replace('.' , '')
                txt = "Insert into automoveis ('%s','%s','%s',%s,'%s',%s);" %(codigo, fabricante , modelo ,ano , pais ,preco)
                saida.write(txt)
                print(txt)
                i+=1
            