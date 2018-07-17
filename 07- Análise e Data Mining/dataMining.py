# -*- coding: utf-8 -*-
import psycopg2
#import pymysql
import matplotlib.pyplot as plt
import pprint
pp = pprint.PrettyPrinter(indent=4)
import os
import tkinter 


'''
	Trabalho pratico - Analise e Data Mining - Parte 1
	Consulta e Analise dos Dados
'''

#######################################################################################
###############################   F U N C O E S   #####################################
#######################################################################################

cursor = None
conex = None
def mysql_connect():
    global cursor,dw
    try:
        DSN = ('localhost','root','root','xmls',3306)
        dw = pymysql.connect(*DSN,charset='utf8')
        cursor = dw.cursor(pymysql.cursors.DictCursor)
    	#print ("Conectado ao BD")
    except:
        print ("erro na conexao BD")
        exit(0)

def conexao():
	global cursor, conex #Precisa deixar como global para que outras funcões possam usar essas variaveis
	try:
		#conecta-se ao banco de dados
		#conex = psycopg2.connect("dbname= '1801TrabalhoTop20181' user='m0n0p0ly' host='200.134.10.32' password='#n0m0n3y#'")
		conex = psycopg2.connect("dbname= 'postgres' user='postgres' host='localhost' password='admin'")
		cursor = conex.cursor() #Abre um cursorsor para executar operacões no BD

	except Exception as e:
		print("Nao conectou ao banco! :(  \nErro: ", e)

def printaNomeCidade():
	
	dadosPerson = "SELECT name, hometown FROM person;"

	try:
		cursor.execute(dadosPerson)

		resultado = cursor.fetchall()

		for row in resultado:
			nome = row[0]
			cidade = row[1]

			print("%s - %s" % (nome, cidade))
	except Exception as e:
		print(e)

#######################################################################################
########################   Q U E S T O E S   S Q L   ##################################
#######################################################################################

def atividade1():
# Qual e a media e desvio padrao dos ratings para artistas musicais e filmes?

#Nessa, tem um caractere indefinido, que não le todas as linhas 

	sql = "SELECT movieuri as artistas_musicais_e_filmes, AVG(rating) as media, STDDEV(rating) as desvio_padrao FROM likesmovie GROUP BY movieUri UNION SELECT bandUri as artistas_musicais_e_filmes, AVG(rating) as media, STDDEV(rating) as desvio_padrao FROM likesmusic GROUP BY bandUri;"


	try:
		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			art = row[0]
			md = float(row[1])
			dp = row[2]

			print("%s - %.2f - %s" % (art, md, dp ))
	except Exception as e:
		print(e)





def atividade2():
# Quais sao os artistas e filmes com o maior rating medio curtidos por pelo menos duas pessoas? Ordenados por rating medio
	sql = "SELECT movieUri as artistas_musicais_e_filmes, AVG(rating) as media , STDDEV(rating) as desvio_padrao FROM likesmovie GROUP BY movieUri HAVING COUNT(movieUri)>1 UNION SELECT bandUri as artistas_musicais_e_filmes, AVG(rating) as media, STDDEV(rating) as desvio_padrao FROM likesmusic GROUP BY bandUri HAVING COUNT(bandUri)>1 ORDER BY 2 DESC"

	try:
		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			art = row[0]
			md = float(row[1])
			dp = float(row[2])

			print("%s - %.2f - %.2f" % (art, md, dp ))
	except Exception as e:
		print(e)


def atividade3():
# Quais sao os 10 artistas musicais e filmes mais populares? Ordenados por popularidade
	sql = "SELECT movieUri as artistas_musicais_e_filmes, COUNT(*) total FROM likesmovie GROUP BY movieUri UNION SELECT bandUri as artistas_musicais_e_filmes, COUNT(*) total FROM likesmusic GROUP BY bandUri ORDER BY 2 DESC LIMIT 10"

	try:
		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			art = row[0]
			total = int(row[1])

			print("%s - %i" % (art, total))
	except Exception as e:
		print(e)

def atividade4():
# Crie uma view chamada conhecidos que represente simetricamente os relacionamentos de conhecidos da turma. Por exemplo, 
# se a conhece b mas b nao declarou conhecer a, a view criada deve conter o relacionamento (b,a) alem de (a,b).
	sql = "CREATE view conhecidos as \
		select distinct k1.person a, k2.person b from knows k1 left join knows k2 on k1.person = k2.colleague having a <> b UNION \
		select distinct  k1.person a, k2.person b from knows k1  right join knows k2 on k1.person = k2.colleague having a <> b \ order by 2 desc,1 desc"

	cursor.execute(sql)
	resultado = cursor.fetchall()
	pp.pprint(resultado)

def atividade5():
# Quais sao os conhecidos (duas pessoas ligadas na view conhecidos) que compartilham o maior numero de filmes curtidos?
# Saida a = luizagner b = erikvamamoto count = 23 + 15 = 38
	sql = " SELECT distinct c.a, COUNT(c.a) ct FROM conhecidos c \
			RIGHT JOIN likesmovie lm ON c.a = lm.person \
			GROUP BY c.a,c.b ORDER BY ct DESC, c.a DESC LIMIT 2 "

def atividade6():
# Qual o número de conhecidos dos conhecidos (usando ConheceNormalizada) para cada integrante do seu grupo?
	sql = "SELECT count(distinct b) FROM conhecidos c WHERE c.a LIKE 'http://utfpr.edu.br/CSB30/2018/1/DI1801patrikymirkoski' or c.a like 'http://utfpr.edu.br/CSB30/2018/1/DI1801gustavopupo' or c.a like 'http://utfpr.edu.br/CSB30/2018/1/DI1801williamsouza' "
def atividade7():
# Construa um gráfico para a função f(x) = (número de pessoas que curtiram exatamente x filmes).
	sql = "SELECT person, count(*) FROM likesmovie GROUP BY person ORDER BY count(*)"
	x = []
	y = []

	cursor.execute(sql)
	resultado = cursor.fetchall()
	#print(resultado)
	
	for row in resultado:
		
		x.append(row[0])
		y.append(row[1])
		
	plt.plot(x, y)
	plt.title("Questao 7")
	plt.ylabel("Curtidas")
	plt.xlabel("Filmes")
	plt.xticks(x, rotation='vertical') # Imprimir eixo x na vertical
	wm = plt.get_current_fig_manager() # Para imprimir em tela cheia
	wm.window.state('zoomed') # Tipo da saida do grafico
	plt.show()

def atividade8():
# Construa um grafico para a funcao f(x) = (numero de filmes curtidos por exatamente x pessoas)
	sql = "SELECT movieUri, count(*) FROM likesmovie GROUP BY movieUri ORDER BY count(*)"
	x = []
	y = []

	cursor.execute(sql)
	resultado = cursor.fetchall()

	for row in resultado:
		x.append(row[0])
		y.append(row[1])
		
	plt.plot(x, y)
	plt.title('Questao 8')
	plt.ylabel("Curtidas")
	plt.xlabel("Filmes")
	plt.xticks(x, rotation='vertical') # Imprimir eixo x na vertical
	wm = plt.get_current_fig_manager() # Para imprimir em tela cheia
	wm.window.state('zoomed') # Tipo da saida do grafico
	plt.show()

def atividade9():
# Qal a disposicao de filmes por cidade natal dos alunos
	sql = "SELECT p.hometown, count(*) FROM person p LEFT JOIN likesmovie lm ON lm.person = p.uri GROUP BY p.hometown ORDER BY COUNT(*) DESC"
	x = []
	y = []

	cursor.execute(sql)
	resultado = cursor.fetchall()

	for row in resultado:
		#print(row)
		x.append(row[0])
		y.append(row[1])
		
	plt.plot(x, y)
	plt.title('Questao 9')
	plt.ylabel("Curtidas")
	plt.xlabel("Cidade")
	plt.xticks(x, rotation='vertical') # Imprimir eixo x na vertical
	wm = plt.get_current_fig_manager() # Para imprimir em tela cheia
	wm.window.state('zoomed') # Tipo da saida do grafico
	plt.show()

def atividade10():
# Disposicao de filmes melhores avaliados por cidade
	sql = "SELECT p.hometown, avg(lm.rating) FROM person p LEFT JOIN likesmovie lm ON lm.person = p.uri GROUP BY p.hometown ORDER BY AVG(lm.rating) DESC"
	x = []
	y = []

	cursor.execute(sql)
	resultado = cursor.fetchall()

	for row in resultado:
		#print(row)
		x.append(row[0])
		y.append(row[1])
		
	plt.plot(x, y)
	plt.title('Questao 10')
	plt.ylabel("Media")
	plt.xlabel("Cidade")
	plt.xticks(x, rotation='vertical') # Imprimir eixo x na vertical
	wm = plt.get_current_fig_manager() # Para imprimir em tela cheia
	wm.window.state('zoomed') # Tipo da saida do grafico
	plt.show()

#######################################################################################
################################   C  R  U  D   #######################################
#######################################################################################

def select():
	print("\nSelecionar tabela:")
	print("\t1. Pessoas")
	print("\t2. Pessoas que curtiram filmes")
	print("\t3. Pessoas que curtiram artistas")
	print("\t4. Pessoas que conhecem pessoas")
	print("\t5. Sair")

	opt = int(input("Escolha a opcao desejada:"))

	if opt == 1:
		sql = "SELECT * FROM person"

		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			print(row)

		select()

	elif opt == 2:
		sql = "SELECT * FROM likesmovie"

		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			print(row)

		select()

	elif opt == 3:
		sql = "SELECT * FROM likesmusic"

		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			print(row)

		select()

	elif opt == 4:
		sql = "SELECT * FROM knows"

		cursor.execute(sql)
		resultado = cursor.fetchall()

		for row in resultado:
			print(row)

		select()

	elif opt == 5:
		menuPrincipal()

	else:
		print("Opcao invalida!")
		select()



def insert():
	print("\nInsira um novo usuario!")
	uri = input("Uri:")
	nome = input("Nome:")
	hometown = input("Cidade:")
	birth = input("Data de nascimento:")
	sql = "INSERT INTO person VALUES ('http://utfpr.edu.br/CSB30/2018/1/DI1801%s','%s','%s','%s') " % (uri, nome, hometown,birth)
	
	try:
		cursor.execute(sql)
		conex.commit()
		print("Usuario inserido com sucesso!")
		menuCRUD()
	except Exception as e:
		print(e)
		insert()

def update():
	opt = input("Digite o usuario que vc deseja atualizar( ou S para sair): ")
	if opt == 'S' or opt == 's':
		return
	sql = "SELECT * FROM person WHERE name LIKE '%s%%' or name like '%s';" % (opt, opt)
	
	try:
		cursor.execute(sql)
		resultado = cursor.fetchall()
		cont = 0
		for row in resultado:
			print(row)
			cont = cont+1

		if cont == 0:
			print("Nenhum nome encontrado!")
			update()
		if cont > 1:
			print("Ha ",cont," nomes como esse. Seja mais preciso!")
			update()
		else:
			print("Digite as novas informacoes!")
			uri = input("Uri:")
			nome = input("Nome:")
			hometown = input("Cidade:")
			birth = input("Data de nascimento:")
			sql = "UPDATE person SET uri = 'http://utfpr.edu.br/CSB30/2018/1/DI1801__%s', name = '%s', hometown = '%s', birthdate = '%s' WHERE name LIKE '%s%%' or name like '%s' " % (uri, nome, hometown,birth, opt, opt) 
			try:
				cursor.execute(sql)
				conex.commit()
				print("Dados atualizados!")
				menuCRUD() 
			except Exception as e:
				print(e)

	except Exception as e:
		print(e)


def delete():
	opt = input("Digite o usuario que vc deseja EXCLUIR( ou S para sair): ")
	if opt == 'S' or opt == 's':
		return
	sql = "SELECT * FROM person WHERE name LIKE '%s%%' or name like '%s';" % (opt, opt)
	try:
		cursor.execute(sql)
		resultado = cursor.fetchall()
		cont = 0
		for row in resultado:
			print(row)
			cont = cont+1
		if cont == 0:
			print("Nenhum nome encontrado!")
			delete()
		if cont > 1:
			print("Há mais nomes como esse. Seja mais preciso!")
			print(cont, " nomes iguais")
			delete()
		else:

			sql = " DELETE FROM person WHERE name LIKE '%s%%' or name = '%s'" % (opt,opt) 
			try:
				cursor.execute(sql)
				conex.commit()
				print("Usuario deletado!")
				menuCRUD()
			except Exception as e:
				print(e)
	except Exception as e:
		print(e)


def menuPrincipal():
	
	print("### MENU PRINCIPAL ###")
	print("1. Para operacoes com o BD")
	print("2. Para Questoes")
	print("3. Para sair")

	menu = int(input("Digite uma opcao:"))


	if menu == 1:
		menuCRUD()

	if menu == 2:
		menuAtividades()

	if menu == 3:
		return



def menuCRUD():

	print("\n")
	print("1. Selecionar")
	print("2. Inserir")
	print("3. Atualizar")
	print("4. Deletar")
	print("5. Sair")
	opc = int(input("Digite uma opcao:"))

	if opc == 1:
		select()
	elif opc == 2:
		insert()
	elif opc == 3:
		update()
	elif opc == 4:
		delete()
	elif opc == 5:
		menuPrincipal()


def menuAtividades():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("1. Qual eh a media e desvio padrao dos ratings para artistas musicais e filmes?")
	print("2. Quais sao os artistas e filmes com o maior rating medio curtidos por pelo menos duas pessoas? Ordenados por rating medio.")
	print("3. Quais sao os 10 artistas musicais e filmes mais populares? Ordenados por popularidade.")
	print("4. Crie uma view chamada ConheceNormalizada que represente simetricamente os relacionamentos de conhecidos da turma. Por exemplo, se a conhece b mas b nao declarou conhecer a, a view criada deve conter o relacionamento (b,a) alem de (a,b).")
	print("5. Quais sao os conhecidos (duas pessoas ligadas na view ConheceNormalizada) que compartilham o maior numero de filmes curtidos?")
	print("6. Qual o numero de conhecidos dos conhecidos (usando ConheceNormalizada) para cada integrante do seu grupo?")
	print("7. Construa um grafico para a funcao f(x) = (numero de pessoas que curtiram exatamente x filmes).")
	print("8. Construa um grafico para a funcao f(x) = (numero de filmes curtidos por exatamente x pessoas).")
	print("*9. Qual a disposicao de filmes por cidade natal dos alunos ")
	print("*10. Disposicao de filmes melhores avaliados por cidade")

	question = int(input("\nDe 1 a 10 - Qual o exercicio desejado?"))

	if question == 1:
		atividade1()
	elif question == 2:
		atividade2()
	elif question == 3:
		atividade3()
	elif question == 4:
		atividade4()
	elif question == 5:
		atividade5()
	elif question == 6:
		atividade6()
	elif question == 7:
		atividade7()
	elif question == 8:	
		atividade8()
	elif question == 9:
		atividade9()
	elif question == 10:
		atividade10()

#######################################################################################
################################    M A I N    ########################################
#######################################################################################


if __name__ == '__main__':
	#mysql_connect()	
	conexao()
	#printaNomeCidade()
	menuPrincipal()



