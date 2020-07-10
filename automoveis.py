# pegar da api as informcacoes
# salvar em um txt: 
# insert into automoveis values (Codigo, Fabricante, Modelo,Ano,Pais,Preco_tabela) 


#http://fipeapi.appspot.com/api/1/[tipo]/[acao]/[parametros].json
#O parametro [tipo] aceita três possíveis valores: carros, motos ou caminhoes.
#
#O parametro [acao] está relacionado ao tipo de dados que você deseja obter.

import time
import json, requests

saida = open('automoveis.txt', 'w')

def get_pais(marca ):
    arquivo = open('marcaAutomoveis.txt','r')
    for linha in arquivo:
        i = linha.index(":")
        if marca in linha[:i]: 
            i+=1
            arquivo.close()
            return(linha[i:-1])
    print("!nao achei %s no arquivo!" %marca)
    pais = input("qual o pais de fabricacao da marca %s :" %marca)
    saida = '%s:%s' %(marca,pais)
    arquivo.write()
    return pais 
    
    
        
            



tipos_automoveis= ['motos' , 'carros' , 'caminhoes']
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
                time.sleep(1)
                print("Rodando ... Inseridos:" ,i)              
                ano_veiculo = el['id']
                
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
                if ano >=2010:
                    txt = "Insert into automoveis ('%s','%s','%s',%s,'%s',%s)" %(codigo, fabricante , modelo ,ano , pais ,preco)
                    print(txt)
                    saida.write(txt)
                    #(Codigo, Fabricante, Modelo,Ano,Pais,Preco_tabela)
                    i+=1
                   
