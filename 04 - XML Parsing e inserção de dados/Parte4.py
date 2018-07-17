# -*- coding: utf-8 -*-
import urllib.request
from xml.dom.minidom import parse, parseString
import xml.dom.minidom
	
import psycopg2.extras

#Deixar como global para que outras funções possam usar essas variaveis
conex = None
cur = None


def conexao():
	global cur, conex 
	try:
		#conecta-se ao banco de dados
		#conex = psycopg2.connect("dbname= '1801TrabalhoTop20181' user='m0n0p0ly' host='200.134.10.32' password='#n0m0n3y#'")
		conex = psycopg2.connect("dbname= 'postgres' user='postgres' host='localhost' password='admin'")
		cur = conex.cursor() #Abre um cursor para executar operações no BD
		print("****Conectou ao banco!****")
	except Exception as e:
		print("Não conectou ao banco! :(  \nErro: ", e)

def Criartabelas():
	global cur, conex

	createPerson = "CREATE TABLE Person( uri VARCHAR(80) NOT NULL, name VARCHAR(80),	hometown VARCHAR(40), bithdate DATE, PRIMARY KEY(uri))"
	createKnows = "CREATE TABLE Knows (person VARCHAR(80) NOT NULL, colleague VARCHAR(80) NOT NULL, PRIMARY KEY(person, colleague), FOREIGN KEY(person) REFERENCES Person(uri) ON DELETE NO ACTION ON UPDATE NO ACTION, FOREIGN KEY(colleague) REFERENCES Person(uri) ON DELETE NO ACTION ON UPDATE NO ACTION )"
	createLikesMusic = "CREATE TABLE LikesMusic (person VARCHAR(80) NOT NULL, bandUri VARCHAR(80) NOT NULL, rating INTEGER, PRIMARY KEY(person, bandUri), FOREIGN KEY(person) REFERENCES Person(uri) ON DELETE NO ACTION ON UPDATE NO ACTION)"
	createLikesMovie = "CREATE TABLE LikesMovie (person VARCHAR(80) NOT NULL, movieUri VARCHAR(80) NOT NULL, rating INTEGER, PRIMARY KEY(person, movieUri), FOREIGN KEY(person) REFERENCES Person(uri) ON DELETE NO ACTION ON UPDATE NO ACTION)"
	createMovie = "CREATE TABLE filmes (movieuri VARCHAR(60), nomefilme VARCHAR(70),sinopse TEXT, rating float, genero VARCHAR(45), produtora varchar(100), data_lancamento DATE, diretor varchar(45), PRIMARY KEY(movieuri))"
	createMusic = "CREATE TABLE musicas(id integer NOT NULL, nome VARCHAR[100],	genero VARCHAR[50],	pais VARCHAR[30],tipo VARCHAR[30],begin1 DATE, end1 VARCHAR[20], PRIMARY KEY(ID))"

	try:
		cur.execute(createPerson)
		cur.execute(createKnows)
		cur.execute(createLikesMusic)
		cur.execute(createLikesMovie)
		cur.execute()

		conex.commit()		
		print("Tabelas criadas com sucesso!")
	except Exception as e:
		print(e)



def InsereBD(Persons, allMusic, knows, allMovie):
	global cur, conex


	#fOR PARA PEGAR OS ATRIBUTOS DE PERSON
	for Person in Persons:
		uri = Person.getAttribute('uri')
		name = Person.getAttribute('name')
		hometown = Person.getAttribute('hometown')
		birthdate = Person.getAttribute('birthdate')
		if birthdate == "":
			birthdate = "1111-11-11"
		try:
			query = "INSERT INTO Person VALUES ('%s','%s','%s','%s')" % (uri, name, hometown, birthdate)
			cur.execute(query)
			conex.commit()
		except:
			continue
	
	print("Dados inseridos em PERSON: OK")

	#fOR PARA PEGAR OS ATRIBUTOS DE AllLikesMusic
	for LikesMusic in allMusic:
		person = LikesMusic.getAttribute('person')
		rating = int(LikesMusic.getAttribute('rating'))
		bandUri = LikesMusic.getAttribute('bandUri')
		#print(person, rating, bandUri)
		try:
			query2 = "INSERT INTO likesmusic VALUES ('%s','%s','%i')" % (person, bandUri, rating)
			cur.execute(query2)
			conex.commit()
		except:
			continue

	print("Dados inseridos em LikesMusic: OK")

	#fOR PARA PEGAR OS ATRIBUTOS DE AllLikesMusic
	for Knows in knows:
		person = Knows.getAttribute('person')
		colleague = Knows.getAttribute('colleague')
		try:
			query = "INSERT INTO knows VALUES ('%s','%s')" % (person,colleague)
			cur.execute(query)
			conex.commit()
		except:
			continue

	print("Dados inseridos em Knows: OK")


	cont = 0
	flag = False

		
		#fOR PARA PEGAR OS ATRIBUTOS DE AllLikesMovie
	for LikesMovie in allMovie:
		cont = cont+1
		person = LikesMovie.getAttribute("person")
		rating = int(LikesMovie.getAttribute('rating'))
		movieUri = LikesMovie.getAttribute('movieUri')

		if cont != 197:
		#Esse IF serve para pular a linha que contém dados duplicados: Likemovie(person,movieUri) na linha 197
			try:
				query2 = "INSERT INTO LikesMovie VALUES ('%s','%s','%i')" % (person,movieUri,rating)
				cur.execute(query2)
				conex.commit()
			except:
				continue
				flag = True

	print("Dados inseridos em LikesMovie: OK")
	if flag:
		print("Deu Ruim!!!")


if __name__ == "__main__":
	conexao()
	Criartabelas()

	pessoa = xml.dom.minidom.parse(urllib.request.urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/person.xml"))
	musica = xml.dom.minidom.parse(urllib.request.urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/music.xml"))
	conhece = xml.dom.minidom.parse(urllib.request.urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/knows.xml"))
	filme = xml.dom.minidom.parse(urllib.request.urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/movie.xml"))

	
	Persons = pessoa.getElementsByTagName("Person")
	allMusic = musica.getElementsByTagName("LikesMusic")
	knows = conhece.getElementsByTagName('Knows')
	allMovie = filme.getElementsByTagName('LikesMovie')



	
	InsereBD(Persons, allMusic, knows, allMovie)
