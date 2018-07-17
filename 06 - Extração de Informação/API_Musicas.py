import musicbrainzngs as m
from bs4 import BeautifulSoup
import json
import pprint
import psycopg2


pp = pprint.PrettyPrinter(indent=4)
m.auth("willdoliver", "Amzivq1!")
m.set_useragent("Example music app", "0.1", "http://example.com/music")
m.set_hostname("beta.musicbrainz.org")


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
		exit(0)



def crawler():

	#Nome da banda/artista
	#Cidade 
	#Genero
	count = 1
	arq = open('ids_artistas.txt', 'r')
	for row in arq.readlines():
		words = row.split(',')
		url = str(words[0])
		genero = words[1]
		try:
			result = m.get_artist_by_id(url, [])
		except:
			try:
				time.sleep(10)
				print('sleep 10')
				result = m.get_artist_by_id(url, [])
			except:
				continue
		#result = m.get_artist_by_id(row, includes=["release-groups"], release_type=["album", "ep"])
		#print (result)
		result = json.dumps(result)
		r = json.loads(result)
		#print(r)
		#print(count)
		# Nome da banda
		try:
			name = r['artist']['name']
			#print(name)
		except:
			name = 'Nome nao encontrado'
			#print(name)
		#print(genero)
		
		try:
			pais = r['artist']['area']['name']	
			#print(pais)
		except:
			pais = 'Cidade nao encontrada'
			#print(pais)

		try:
			# Tipo da banda
			tipo = r['artist']['type']
			#print(tipo)	
		except:
			tipo = 'Tipo nao encontrado'
			#print(tipo)	

		try:
			life_band = r['artist']['life-span']
			begin = life_band['begin']
			end = life_band['end']
			#print(begin)
			#print(end)
		except:
			try:
				life_band = r['artist']['life-span']
				begin = life_band['begin']
				end = 'Banda ativa'
				#print(begin)
				#print(end)
			except:
				begin = 'Inicio nao encontrado'
				end = 'Banda ativa'
				#print(begin)
				#print(end)
		#print('\n')
		
		insereBD(count, name, genero, pais, tipo, begin, end)
		

		count += 1
		
def insereBD(count, name, genero, pais, tipo, begin, end):
	global cur, conex
	#Tratar as variáveis com '
	name = name.replace("'","")
	query = "INSERT INTO musicas (id, nome, genero, pais, tipo, begin1, end1) VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s' )" % (count, name, genero, pais, tipo, begin, end)
	#print(query)

	if len(begin) > 12 or len(begin) < 8:
		begin = "null"
		query = "INSERT INTO musicas (id, nome, genero, pais, tipo, begin1, end1) VALUES ('%d', '%s', '%s', '%s', '%s', %s, '%s' )" % (count, name, genero, pais, tipo, begin, end)

	try:
		cur.execute(query)
		conex.commit()
	except Exception as e:
		print(e)

#sertanejo
#rock
#pop
#rap
#funk
# Para encontrar mais ids de artista por categoria
#result = m.search_artists(query='tag:funk')
#for artist in result['artist-list']:
#	print(u"{id}".format(id=artist['id']))
#	print(u"{id}: {name}".format(id=artist['id'], name=artist["name"]))


if __name__ == '__main__':
	
	conexao()
	crawler()

