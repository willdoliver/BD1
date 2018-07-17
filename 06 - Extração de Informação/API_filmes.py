import requests
from bs4 import BeautifulSoup
import tmdbsimple as tmdb
import pprint
import json
import psycopg2

pp = pprint.PrettyPrinter(indent=4)
key = "?api_key=a913ee104db6b795d20852a9ed989036"

#id_filme(int 10), 
#nome_filme(varchar(100)), 
#sinopse(text), 
#rating(float), 
#genero(varchar(45))
#produtora(varchar(100))
#data_lancamento(datetime)
#diretor(varchar(45))
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


def crawler_API_filmes():
	print("entrou no crawler_API_filmes")
	num = 1
	soma = 0
	qtde_filmes = 250
	while 1:
		try:
			vetDirector = []
			url = "https://api.themoviedb.org/3/movie/"+str(num)+key+"&append_to_response=credits,release_dates"
			#print(url)
			
			request_page =  requests.get(url)
			#soup_page = BeautifulSoup(request_page.text,'html.parser')
			prd_meta = json.loads(request_page.text)
			id_movie = prd_meta['id']
			#print(id_movie)

			title = prd_meta['title']
			#print(title)

			overview = prd_meta['overview']
			#print(overview)

			popularity = prd_meta['popularity']
			#print(popularity)

			genres = prd_meta['genres'][0]['name']
			#print(genres)

			production_companies = prd_meta['production_companies'][0]['name']
			#print(production_companies)

			release_dates = prd_meta['release_dates']['results'][0]#['release_dates']['release_date']
			release_dates = release_dates['release_dates'][0]['release_date']
			#print(release_dates)

			director = prd_meta['credits']['crew']
			# Encontra o nome do diretor pelo vetor
			vetDirector.append(director)
			for item in vetDirector:
				director = item[1]['name']
			#print(director)
			#print('\n')

			num += 1
			soma += 1

			insereBD_API_filmes(url, title, popularity, genres, production_companies, release_dates, director)

			# 
			if soma == qtde_filmes:
				break
		except:
			#print("Erro")
			num += 1
			continue


def insereBD_API_filmes(url, title, popularity, genres, production_companies, release_dates, director):
	global cur, conex

	title = title.replace("'","")
	try:
		query = "INSERT INTO filmes (movieuri, nomefilme, rating, genero, produtora, data_lancamento, diretor) VALUES ('%s','%s', '%f', '%s', '%s', '%s', '%s' )" % (url, title, popularity, genres, production_companies, release_dates, director)
		cur.execute(query)
		conex.commit()
		#print("BD ok")
	except Exception as e:
		print(e)

if __name__ == '__main__':
	conexao()
	crawler_API_filmes()


	### TRATAR char ' que tem em título, produtora ou diretor. Se der boa, incluir tbm sinopse 