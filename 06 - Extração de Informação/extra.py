# -*- coding: utf-8 -*-
import re
import os
import json
import urllib2
import pymysql
import requests
import psycopg2
import pprint
pp = pprint.PrettyPrinter(indent=4)
from bs4 import BeautifulSoup
import string


alfabeto = list(string.ascii_lowercase)
padrao = "http://cinepop.com.br/filme/filmes-letra-"

### = open('result.txt', 'w')
# Loop para percorrer filmes com todas as letras do alfabeto
for letra in alfabeto:
	# Requisicao para pegar as categorias de filmes
	url_filme = padrao + letra
	request_page =  requests.get(url_filme)
	soup_page = BeautifulSoup(request_page.text,'html.parser')
	filmes = soup_page.find('div', id='content')
	filmes_pagina = filmes.find_all('h2')

	# Loop para pegar cada url da pagina e capturar as informacoes de cada filme
	for item in filmes_pagina:
		filmes_pagina = item.find('a')
		url = filmes_pagina['href']
		print("Link do filme: " +url)
		###.write(url)
		###.write('\n')

		request_movie =  requests.get(url)
		soup_movie = BeautifulSoup(request_movie.text,'html.parser')

		page = soup_movie.find('div', id='content')

		movie_img = page.find('img')
		movie_img = movie_img['src']
		print("Link da imagem : "+movie_img)
		###.write(movie_img)
		###.write('\n')

		movie_name = page.find('h1')
		movie_name = movie_name.text
		print("Nome do filme: "+movie_name)
		###.write(movie_name)
		###.write('\n')		

		try:
			ratingValue = page.find('div', itemprop='aggregateRating')
			ratingCount = ratingValue.find('span', itemprop='ratingCount')
			ratingCount = ratingCount.text
			ratingValue = ratingValue.find('span', itemprop='ratingValue')
			ratingValue = ratingValue.text
		except:
			ratingCount = 0
			ratingValue = 0
		print("Quantidade de pessoas que votaram : " + str(ratingCount))
		print("Nota : " +str(ratingValue))
		###.write(ratingCount)
		###.write('\n')		
		###.write(ratingValue)
		###.write('\n')

		paragrafos = page.find_all('p')
		aux = []
		for p in paragrafos:
			#print(p)
			aux.append(p)

		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Sinopse)\b', str(i))
				var += 1
			except:
				continue
			#print(find)
			if 'Sinopse' in find:
				try:
					sinopse = aux[var]
					sinopse = sinopse.text
					print(sinopse)
				except:
					sinopse = ''
					print(sinopse)
				###.write(sinopse)
				###.write('\n')

		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Curiosidades)\b', str(i))
				var += 1
			except:
				continue
			#print(find)
			if 'Curiosidades' in find:
				curiosidades = aux[var]
				print(curiosidades)
				###.write(curiosidades)
				###.write('\n')

		# Direcao - OK
		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Direção)\b', str(i))
				if 'Direção' in find:
					direcao = aux[var]
					direcao = direcao.find('a')
					direcao = direcao.text
					print(direcao)
					###.write(direcao)
					###.write('\n')
				var += 1
			except:
				continue		

		# Gênero
		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Gênero)\b', str(i))
				if 'Gênero' in find:
					genero = aux[var]
					genero = genero.find('a')
					print(genero)
					###.write(genero)
					###.write('\n')
				var += 1
			except:
				continue
		
		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Duração)\b', str(i))
				if 'Duração' in find:
					duracao = aux[var]
					duracao = re.findall(r'[0-9]+', str(duracao))
					print(duracao)
					###.write(duracao)
					###.write('\n')
				var += 1
			except:
				continue
		
		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Distribuidora)\b', str(i))
				if 'Distribuidora' in find:
					distribuidora = aux[var]
					distribuidora = distribuidora.find('a')
					distribuidora = distribuidora.text
					print(distribuidora)
					###.write(distribuidora)
					###.write('\n')
				var += 1
			except:
				continue
		
		var = 0
		for i in aux:
			try:
				find = re.findall(r'[^-]\b(Estreia)\b', str(i))
				if 'Estreia' in find:
					estreia = aux[var]
					estreia = estreia.text
					estreia = re.sub(r'^[Estreia: ]+', '', estreia)
					print(estreia)
					###.write(estreia)
					###.write('\n')
				var += 1
			except:
				continue

		#exit(0)

# Musicas
# https://www.ufrgs.br/psicoeduc/variados/enderecos-musicas/