from banco import getConect,Error,errorcode

import time
import json, requests

#Função: insereAuto
#
#Descrição da função:
#   Insere no banco my a dupla de automoveis
#
#Parâmetros
#   CodigoAuto  
#   Fabricante
#   Modelo
#   Pais
#   Preco
#
def insereAuto(codigo , fabricante, modelo ,ano , pais, preco , connection = getConect()):
    try:
        sql ="""Inserte into automoveis  
                values (%s,%s,%s,%s,%s,%s)
                """
        cursor = connection.cursor(prepared = True)
        cursor.execute(sql ,())
        rs = cursor.fetchall()
        cursor.close()
        return rs
    except Error as e:
        print("Erro ao procurar o nome dos jogadores", e)
        return 1
    

def get_pais(marca ):
    arquivo = open('marcaAutomoveis.txt','r')
    for linha in arquivo:
        i = linha.index(":")
        if marca in linha[:i]: 
            i+=1
            arquivo.close()
            return(linha[i:-1])
    return None
    
#Função: buscaMarca
#
#Descrição da função:
#   Busca as marcas de automoveis validos 
#
#Parâmetros
#   void
#    
def buscaMarca():
    #tipos_automoveis= ['motos' , 'carros' , 'caminhoes']
    tipos_automoveis= ['carros']
    i=0
    for tipo in tipos_automoveis:

        #A api da tabela FIPE bloqueia o usuario a pesquisar mais de 60 vezes por minuto
        #por isso a cada pesquisa vamos esperar 1
        html_marca = "http://fipeapi.appspot.com/api/1/%s/marcas.json" %tipo
        time.sleep(1)
        
        api_marca = requests.get(html_marca)
        json_marca = json.loads(api_marca.content)
        marcas =[]
        for el in json_marca:
            fabricante = {'id':el['id'] , 'name': el['name']}
            marcas.append(fabricante)
        return marcas
            

#Função: BuscaAuto
#
#Descrição da função:
#   Busca na api da tabela fipe automoveis validos 
#   Salva no banco 
#
#Parâmetros
#   Ano de comeco
#   marca = ALL
#
def BuscaAuto():

    for marca in json_marca:
        print(marca)
        id_marca = marca['id']
        pais = get_pais(marca['name'])
        print(pais)
        break
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
                #pais = get_pais(automovel['marca'])
                codigo =automovel['fipe_codigo']
                fabricante = automovel['marca']
                modelo = automovel['veiculo']
                ano = int(automovel['ano_modelo'])
                preco = automovel['preco'][3:-3]
                preco = preco.replace('.' , '')
                if ano >=2010:
                    #sql = "Insert into automoveis ('%s','%s','%s',%s,'%s',%s)" %(codigo, fabricante , modelo ,ano , pais ,preco)
                    #print(txt)
                    #saida.write(txt)
                    #(Codigo, Fabricante, Modelo,Ano,Pais,Preco_tabela)
                    i+=1

for el in buscaMarca():
    print(el)
