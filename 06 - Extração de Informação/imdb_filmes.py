import musicbrainzngs as m
from bs4 import BeautifulSoup
import requests
import json
import re
import pprint
import psycopg2

pp = pprint.PrettyPrinter(indent=4)
 

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



#sinopse(text), 
#produtora(varchar(100))
#diretor(varchar(45))
def crawler():

	arq = open('imdb_filmes.txt', 'r')
	for row in arq.readlines():
		url = row
		
		request_page =  requests.get(url)
		soup_page = BeautifulSoup(request_page.text,'html.parser')	

		print(url)
		title_wrapper = soup_page.find('div', class_='title_wrapper')
		name = title_wrapper.find('h1', itemprop='name')
		name = name.text
		print (name)

		rating = soup_page.find('span', {'itemprop':'ratingValue'})
		rating = rating.text
		print (rating)

		year = title_wrapper.find('span', {'id':'titleYear'})
		year = year.text
		year = re.findall(r'[\w]+', year)
		year = ''.join(year)
		print(year)

		genero = title_wrapper.find('span', itemprop='genre')
		genero = genero.text
		print (genero)

		group2 = soup_page.find('div', {'class':'plot_summary'})

		sinopse = group2.find('div', {'class':'summary_text'})
		sinopse = sinopse.text
		sinopse = re.sub(r' +', ' ', sinopse)
		print (sinopse)
		
		director = group2.find('span', {'itemprop':'director'})
		director = director.text
		print (director)
		
		print('\n')



if __name__ == '__main__':
	conexao()
	crawler()