# -*- coding: utf-8 -*-
import urllib
from xml.dom.minidom import parse, parseString
import xml.dom.minidom
import sys
#import pymysql
import psycopg2
import psycopg2.extras
import csv
import pprint
pp = pprint.PrettyPrinter(indent=4)

conn = None
cursor = None


'''def mysql_connect():
    global cursor,dw
    try:
        DSN = ('localhost','root','root','xmls',3306)
        dw = pymysql.connect(*DSN,charset='utf8')
        cur = dw.cursor(pymysql.cursors.DictCursor)
    except:
        print ("erro na conexao BD")
'''

def conectapgAdmin():
    global conn, cursor
    try:
        #conn = psycopg2.connect("dbname='1801TrabalhoTop20181' user='m0n0p0ly' host='200.134.10.32' password='#n0m0n3y#'")
        conn = psycopg2.connect("dbname= 'postgres' user='postgres' host='localhost' password='admin'")
        cursor = conn.cursor()
        print("Conectado ao Banco!")
    except:
        print("Erro ao conectar no banco.")
    return


#Create Line
def insert(uri, name, hometown):
    global conn, cursor
    strdeenvio = "INSERT INTO persons VALUES ('%s', '%s', '%s')" % (uri, name, hometown)
    cursor.execute(strdeenvio)
    cursor = conn.cursor()
    print ("Insert com sucesso: Uri ", uri)

#Read OK
def select(opc,sql):

    if opc == "1":
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                nome = row[1]
                cidade = row[2] 
                
                print("%s - %s" % (nome, cidade))
        except Exception as e:
            print(e)

    if opc == "2":
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                movie = row[1]
                
                print(movie)
        except Exception as e:
            print(e)        
 
    if opc == "3":
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                music = row[1]
                
                print(music)
        except Exception as e:
            print(e) 

    if opc == "4":
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                k1 = row[0]
                k2 = row[1]
                
                print("%s\tCONHECE\t %s" % (k1,k2))
        except Exception as e:
            print(e)    

     
    #pp.pprint(rows)

#Update
def update(uri, new_city):
    global conn, cursor
    strdeenvio = "UPDATE `persons` SET `hometown`='%s' WHERE `uri`='%s'" % (new_city, uri)
    cursor.execute(strdeenvio)
    cursor = conn.cursor()
    print ("Uri ", uri, " alterado cidade para ",new_city)


#Delete
def delete(uri):
    global conn, cursor
    #Se nao tiver mostra a msg mas nao faz nada
    strdeenvio = "DELETE FROM `persons`  WHERE `uri`='%s'" % uri
    cursor.execute(strdeenvio)
    cursor = conn.cursor()
    print ("Uri ", uri, " deletado com sucesso")




def tipoSelect():
    
    opc = input("\tDigite um numero de acordo com a opcao desejada\n\t(1) - SELECT em Person\n\t(2) - SELECT em Likesmovie \n\t(3) - SELECT em Likesmusic \n\t(4) - SELECT em Knows\n\t")

    if opc == "1":
        sql = "SELECT * FROM person"
        select(opc, sql)
    
    elif opc == "2":
        sql = "SELECT * FROM Likesmovie"
        select(opc, sql)

    elif opc == "3":
        sql = "SELECT * FROM Likesmusic"
        select(opc, sql)

    elif opc == "4":
        sql = "SELECT * FROM knows"
        select(opc, sql)

    else:
        print("Valor invalido!")   


if __name__ == "__main__":
#Selecionar um banco para conexao
    conectapgAdmin()
    #mysql_connect()

    opc = input("Digite um numero de acordo com a opcao desejada\n(1) - INSERT\n(2) - SELECT \n(3) - UPDATE \n(4) - DELETE\n")

    if opc == "1":
        insert()
        #insert("http://utfpr.edu.br/CSB30/2018/1/DI1801williamsouza2","Will","Veneza")

    elif opc == "2":
        tipoSelect()

    elif opc == "3":
        update()
        #update("http://utfpr.edu.br/CSB30/2018/1/DI1801williamsouza2", "Bogota")

    elif opc == "4":
        delete()
        #delete("http://utfpr.edu.br/CSB30/2018/1/DI1801williamsouza2")

    else:
        print("Valor invalido!")
