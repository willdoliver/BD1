# -*- coding: utf-8 -*-
import urllib
from xml.dom.minidom import parse, parseString
import xml.dom.minidom
import sys
import pprint
import psycopg2
import psycopg2.extras


conn = None
cur = None


def conectapgAdmin():
    global conn, cur
    try:
        conn = psycopg2.connect("dbname='1801TrabalhoTop20181' user='m0n0p0ly' host='200.134.10.32' password='#n0m0n3y#'")
        cur = conn.cursor()
        print("Conectado ao Banco!")
    except:
        print("Nao foi possivel conectar-se com a database.")
    return


def criaTables():
    global cur
    comandoPessoa = "CREATE TABLE Persons ( uri VARCHAR(150) NOT NULL, name VARCHAR(80) NOT NULL, hometown VARCHAR(50) NOT NULL, PRIMARY KEY(uri));"
    comandoMusica = "CREATE TABLE LikesMusic ( person VARCHAR(150) NOT NULL, rating INTEGER NOT NULL, bandUri VARCHAR(150) NOT NULL, PRIMARY KEY(person, bandUri), FOREIGN KEY(person) REFERENCES Persons(uri) ON DELETE NO ACTION ON UPDATE NO ACTION );"
    comandoFilme = "CREATE TABLE LikesMovie ( person VARCHAR(150) NOT NULL, rating INTEGER NOT NULL, movieUri VARCHAR(150) NOT NULL, PRIMARY KEY(person, movieUri), FOREIGN KEY(person) REFERENCES Persons(uri) ON DELETE NO ACTION ON UPDATE NO ACTION );"
    comandoConhecido = "CREATE TABLE Knows ( person VARCHAR(150) NOT NULL, colleague VARCHAR(150) NOT NULL, PRIMARY KEY(person, colleague), FOREIGN KEY(person) REFERENCES Persons(uri) ON DELETE NO ACTION ON UPDATE NO ACTION, FOREIGN KEY(colleague) REFERENCES Persons(uri) ON DELETE NO ACTION ON UPDATE NO ACTION );"
    cur.execute(comandoPessoa)
    cur.execute(comandoMusica)
    cur.execute(comandoFilme)
    cur.execute(comandoConhecido)

    conn.commit()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    


def enviapgAdmin(dados, select):
    global cur
    global conn
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if select == 1:
        for pessoa in pessoas:
            uri = pessoa.getAttribute("uri")
            name = pessoa.getAttribute("name")
            hometown = pessoa.getAttribute("hometown")
            strdeenvio = "INSERT INTO Persons VALUES ('%s', '%s', '%s')" % (uri, name, hometown)
            try:
                cur.execute(strdeenvio)
                conn.commit()
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            except Exception as e:
                print(e)

    if select == 2:
        for musica in musicas:
            person = musica.getAttribute("person")
            rating = musica.getAttribute("rating")
            bandUri = musica.getAttribute("bandUri")
            strdeenvio = "INSERT INTO LikesMusic VALUES ('%s', '%s', '%s')" % (person, rating, bandUri)
            try:
                cur.execute(strdeenvio)
                conn.commit()
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            except Exception as e:
                print(e)

    if select == 3:
        for filme in filmes:
	    
            person = filme.getAttribute("person")
            rating = filme.getAttribute("rating")
            movieUri = filme.getAttribute("movieUri")
            strdeenvio = "INSERT INTO LikesMovie VALUES ('%s', '%s', '%s')" % (person, rating, movieUri)
            try:
                cur.execute(strdeenvio)
                conn.commit()
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            except Exception as e:
                print(e)

	    

    if select == 4:
        for conhecido in conhecidos:
            person = conhecido.getAttribute("person")
            colleague = conhecido.getAttribute("colleague")
            strdeenvio = "INSERT INTO Knows VALUES ('%s', '%s')" % (person, colleague)
            try:
                cur.execute(strdeenvio)
                conn.commit()
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            except Exception as e:
                print(e)
    return


def parseiaXML(url):
    XML = xml.dom.minidom.parse(urllib.urlopen(url))
    print
    "xml %s funcionando" % url
    return XML.documentElement;


if __name__ == "__main__":
    conectapgAdmin()
    criaTables()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur.execute("""SELECT person FROM LikesMovie;""")
    #rows = cur.fetchall()
    #for row in rows:
    #	print "", row['person']
    pessoasXML = parseiaXML('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/person.xml')
    musicasXML = parseiaXML('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/music.xml')
    filmesXML = parseiaXML('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/movie.xml')
    conhecidosXML = parseiaXML('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/knows.xml')
    pessoas = pessoasXML.getElementsByTagName('Person')
    musicas = musicasXML.getElementsByTagName('LikesMusic')
    filmes = filmesXML.getElementsByTagName('LikesMovie')
    conhecidos = conhecidosXML.getElementsByTagName('Knows')
    enviapgAdmin(pessoas, 1)
    enviapgAdmin(musicas, 2)
    enviapgAdmin(filmes, 3)
    enviapgAdmin(conhecidos, 4)	

