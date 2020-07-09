

__all__ = ["getConect","conectBD","disconectBD"]
#teste2

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

_conexao = []


#Função: getConect
#
#Descrição da função:
#   Pega a conexão feita com o myslq 
#
#Parâmetro:
#   void                  
#
#Valor retornado
#Se executou corretamente: 
#   retorna a conexao
#
def getConect (conexao =  _conexao):
    if conexao == []:
        conectBD()
    return conexao[0]

#cria o banco de dados
def criaBD ():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='root')
        sql = ["CREATE SCHEMA carros ;",
            "USE carros;",

            """CREATE TABLE automoveis (
            Codigo varchar(9) NOT NULL
            ,Fabricante varchar(15)
            ,Modelo varchar(50)
            ,Ano NUMERIC(4) NOT NULL
            ,Pais VARCHAR(15)
            ,Preco_tabela NUMERIC(8)
            );""",
            """ALTER TABLE automoveis
            ADD CONSTRAINT PK_automoveis PRIMARY KEY (Codigo, Ano)
            ;""",
            """CREATE TABLE consumidores(
            CPF VARCHAR(14) NOT NULL
            ,Nome VARCHAR(15)
            ,Sobrenome varchar(15)
            ,Data_nascimento DATE
            ,Estado CHAR(2)
            );""",
            """ALTER TABLE consumidores
            ADD CONSTRAINT PK_consumidores PRIMARY KEY (CPF)
            ;""",
            """CREATE TABLE revendedoras (
            CNPJ VARCHAR(18) NOT NULL
            ,Nome CHAR(20)
            ,CPFproprietario VARCHAR(14)
            ,Estado CHAR(2)
            );""",
            """ALTER TABLE revendedoras
            ADD CONSTRAINT PK_revendedora PRIMARY KEY (CNPJ)
            ;""",
            """CREATE TABLE garagens (
            CNPJrevenda VARCHAR(18) NOT NULL
            ,CodigoAuto VARCHAR(9) NOT NULL
            ,AnoAuto NUMERIC(4) NOT NULL
            ,Quantidade INT NOT NULL
            ,CHECK (quantidade > 0)
            );""",
            """ALTER TABLE garagens
            ADD CONSTRAINT PK_garagem PRIMARY KEY (CNPJrevenda, CodigoAuto, AnoAuto)
            ,ADD CONSTRAINT FK_garagem_revendedora FOREIGN KEY (CNPJrevenda)
            REFERENCES revendedoras (CNPJ)
            ,ADD CONSTRAINT FK_garagem_automoveis FOREIGN KEY (CodigoAuto , AnoAuto)
            REFERENCES automoveis (Codigo , Ano)
            ;""",
            """CREATE TABLE negocios(
            CPFcomprador VARCHAR(14) NOT NULL
            ,CNPJrevenda VARCHAR(18) NOT NULL
            ,CodigoAuto VARCHAR(9) NOT NULL
            ,AnoAuto numeric(4) NOT NULL
            ,Data DATE
            ,Preco numeric(8)
            );""",
            """ALTER TABLE negocios
            ADD CONSTRAINT PK_negocios PRIMARY KEY (CPFcomprador, CNPJrevenda,
            CodigoAuto, AnoAuto)
            ,ADD CONSTRAINT FK_negocios_revendedora FOREIGN KEY (CNPJrevenda)
            REFERENCES revendedoras (CNPJ)
            ,ADD CONSTRAINT FK_negocios_automoveis FOREIGN KEY (CodigoAuto , AnoAuto)
            REFERENCES automoveis (Codigo , Ano)
            ,ADD CONSTRAINT FK_negocios_consumidores FOREIGN KEY (CPFcomprador)
            REFERENCES consumidores (CPF)
            ;"""]

        for el in sql:
            cursor = connection.cursor()
            cursor.execute(el)
            connection.commit()
        cursor.close()
        connection.close()
        print("Banco criado com sucesso")
        conectBD()
        return 0
    except Error as e:
        print("Erro ao criar o banco de dados", e)
        return 1


#Função: conectBD

#Descrição da função:
#Inicia a conexão com o mysql
# 
#Parâmetros:
#(void)       
#             
#Valor retornado:
#Se executou corretamente: 
#retorna 0
#
#Se ocorreu algum erro: 
#retorna 1
#
def conectBD ():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='carros',
                                            user='root',
                                            password='root')
        _conexao.append(connection)
        print("conectado com BD")
        return 0
    except Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            if criaBD():
                return 2
            else:
                return 0
        print("Erro de conexão", err)
        return 1
    

#Função: disconectBD
#
#Descrição da função:
#   finaliza a conexão do Mysql 
#
#Parâmetros
#   (void)             
#       
#Valor retornado
#Se executou corretamente: 
#   retorna 0
#
#Se ocorreu algum erro: 
#   retorna 1
#   caso  não tenha uma conexão ativa antes
#
def disconectBD(connection = _conexao):
    if (connection[0].is_connected()):
        connection[0].close()
        connection.clear()
        print("Conexao encerrada")
        return 0
    print("Sem Conexao")
    return 1
    

#Função: criaJogador
#
#Descrição da função:
#cria um jogador com Id e nome      
#
#Parâmetros
#nome do jogador e conexão com o banco                  
#
#Valor retornado
#Se executou corretamente: 
#retorna 0
#Caso o jogador seja criado 
#
#Se ocorreu algum erro: 
#retorna 1
#caso  não consiga criar um jogador.

def criaJogador( name, connection ):
    try:
        
        sql = """INSERT INTO yatzy.jogador
                (nome)
                VALUES (%s);"""
        
        cursor = connection.cursor(prepared = True)
        cursor.execute(sql , (name,))
        connection.commit()
        print(cursor.rowcount, "Registro inserido")
        cursor.close()
        return 0
    except Error as e:
        print("Erro de conexão", e)
        return 1


