# -*- coding: utf-8 -*-
import json

with open('musicas.txt') as json_file:
	data = json.load(json_file)
	padrao = data['bandas'][0]
	id_a = padrao['id']
	nome = padrao['nome']
	genero = padrao['genero']
	pais = padrao['pais']
	tipo = padrao['tipo']
	begin = padrao['begin1']
	end = padrao['end1']
	print(id_a)
	print(nome)
	print(genero)
	print(pais)
	print(tipo)
	print(begin)
	print(end)
	exit(0)
