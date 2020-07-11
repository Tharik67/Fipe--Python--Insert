

import time
import json, requests


save = open('cont.txt' , 'w')
saida = open('automoveis.txt', 'w')

def get_pais(marca):
    arquivo = open('marcaAutomoveis.txt','r+')
    marca = marca.upper()
    for linha in arquivo:
        i = linha.index(":")
        if marca in linha[:i]: 
            i+=1
            arquivo.close()
            return(linha[i:-1])
        
    print("!nao achei %s no arquivo!" %marca)
    pais = input("qual o pais de fabricacao da marca %s :" %marca)
    dic = '\n%s:%s' %(marca,pais)
    arquivo.write(dic)
    return pais 
    
    
#tipos_automoveis= ['motos' , 'carros' , 'caminhoes']
tipos_automoveis= ['carros']


i=0

for tipo in tipos_automoveis:
    time.sleep(1)
    
    html_marca = "http://fipeapi.appspot.com/api/1/%s/marcas.json" %tipo

    api_marca = requests.get(html_marca)
    json_marca = json.loads(api_marca.content)
    
    for marca in json_marca:
        
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

                if int(ano_veiculo[:-2]) < 2010:
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
                txt = "Insert into automoveis ('%s','%s','%s',%s,'%s',%s)" %(codigo, fabricante , modelo ,ano , pais ,preco)
                saida.write(txt)
                i+=1
            