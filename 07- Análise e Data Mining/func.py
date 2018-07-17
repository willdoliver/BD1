# -*- coding: utf-8 -*-
import urllib
import sys
import matplotlib
import pymysql
import psycopg2
import psycopg2.extras
import pprint
pp = pprint.PrettyPrinter(indent=4)

conn = None
cursor = None


def mysql_connect():
    global cursor,dw
    try:
        DSN = ('localhost','root','root','xmls',3306)
        dw = pymysql.connect(*DSN,charset='utf8')
        cursor = dw.cursor(pymysql.cursors.DictCursor)
    except:
        print ("erro na conexao BD")


def conectapgAdmin():
    global conn, cursor
    try:
        conn = psycopg2.connect("dbname='1801TrabalhoTop20181' user='m0n0p0ly' host='200.134.10.32' password='#n0m0n3y#'")
        cursor = conn.cursor()
        print("Conectado ao Banco!")
    except:
        print("Erro ao conectar no banco.")
    return

def select(num):
# 7. Número de pessoas que curtiram exatamente x filmes
    if num == 7:
        selec =  """SELECT *,COUNT(*) pessoas 
                    FROM 
                        (SELECT COUNT(*) num_filmes
                        FROM persons p
                            LEFT JOIN likesmovie lm ON lm.person = p.uri
                        GROUP BY p.name
                        ORDER BY COUNT(*) DESC) asd
                    GROUP BY 1
                    ORDER BY 1 DESC;"""
# 8. Número de filmes curtidos por exatamente x pessoas
    if num == 8:
        selec = """ SELECT lm.movieUri, COUNT(*) num_filmes
                    FROM likesmovie lm 
                        LEFT JOIN persons p ON lm.person = p.uri
                    GROUP BY lm.movieUri
                    ORDER BY COUNT(*) DESC """
# 9.1 A disposicao de filmes por cidade natal dos alunos      
    if num == 9.1:
        selec = """ SELECT p.hometown, COUNT(*)
                    FROM persons p
                        LEFT JOIN likesmovie lm ON lm.person = p.uri
                    GROUP BY p.hometown
                    ORDER BY COUNT(*) DESC"""
# 9.2 disposicao de filmes melhores avaliados por cidade
    if num == 9.2:
        selec = """ SELECT p.hometown, AVG(lm.rating)
                    FROM persons p
                        LEFT JOIN likesmovie lm ON lm.person = p.uri
                    GROUP BY p.hometown
                    ORDER BY AVG(lm.rating) DESC"""

    cursor.execute(selec)
    rows = cursor.fetchall()
    # Montar o grafico
    for row in rows:
       pp.pprint (row)

if __name__ == "__main__":
#Selecionar um banco para conexao
    #conectapgAdmin()
    mysql_connect()
    select(7)
    #select(8)
    #select(9.1)
    #select(9.2)
