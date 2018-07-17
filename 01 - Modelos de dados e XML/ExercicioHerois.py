#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#Usando ElementTree para trabalhar com arquivos XML


from xml.etree import ElementTree as et


conteudo = et.parse('campeonato.xml')

lista_equipes = conteudo.findall("equipe")



for equi in lista_equipes:
    print ("Nome da equipe: ", equi.find("descricao").text)

'''

#!/usr/bin/python


#Usando xml.dom.minidom para trabalhar com arquivos XML
from xml.dom.minidom import parse
import xml.dom.minidom
import csv

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("marvel_simplificado.xml")

universe = DOMTree.documentElement
if universe.hasAttribute("name"):
   print ("Root element : %s" % universe.getAttribute("name"))

# Get all the heroes in the universe
heroes = universe.getElementsByTagName("hero")



fileHerois = open('herois.csv', 'w')
herois_bad = open('herois_bad.csv', 'w')
herois_good = open('herois_good.csv', 'w')

                        #DELIMITER: usar ";" para separar cada celular  LINETERMINATOR: usar para pular apenas uma linha 
writerFile = csv.writer(fileHerois, delimiter = ";" ,lineterminator = '\r', quoting =csv.QUOTE_MINIMAL)
badFile = csv.writer(herois_bad, delimiter = ';', lineterminator = '\r', quoting = csv.QUOTE_MINIMAL)
goodFile = csv.writer(herois_good, delimiter = ';', lineterminator = '\r', quoting = csv.QUOTE_MINIMAL)

#cabeçalho das 3 planilhas
writerFile.writerow(["Id", "Nome", 'Popularidade', 'Time', 'Genero', 'Altura', 'Peso', 'Localizacao', 'Inteligencia', 'Forca', 'Velocidade',
     'Durabilidade', 'Energia', 'Skils' ])
badFile.writerow(["Id", "Nome", 'Popularidade', 'Time', 'Genero', 'Altura', 'Peso', 'Localizacao', 'Inteligencia', 'Forca', 'Velocidade',
     'Durabilidade', 'Energia', 'Skils' ])
goodFile.writerow(["Id", "Nome", 'Popularidade', 'Time', 'Genero', 'Altura', 'Peso', 'Localizacao', 'Inteligencia', 'Forca', 'Velocidade',
     'Durabilidade', 'Energia', 'Skils' ])


cont = 0
contBad = 0
contGood = 0
contpeso = 0

for hero in heroes:

   id  = hero.getAttribute('id')
   nome = hero.getElementsByTagName('name')[0]
   popularidade = hero.getElementsByTagName('popularity')[0]
   time = hero.getElementsByTagName('alignment')[0]
   genero = hero.getElementsByTagName('gender')[0]
   altura = hero.getElementsByTagName('height_m')[0]
   peso = hero.getElementsByTagName('weight_kg')[0]
   localizacao = hero.getElementsByTagName('hometown')[0]
   inteligencia = hero.getElementsByTagName('intelligence')[0]
   forca = hero.getElementsByTagName('strength')[0]
   velocidade = hero.getElementsByTagName('speed')[0]
   durabilidade = hero.getElementsByTagName('durability')[0]
   energia = hero.getElementsByTagName('energy_Projection')[0]
   Skils = hero.getElementsByTagName('fighting_Skills')[0]


   cont +=1
   contpeso += int (peso.childNodes[0].data)

   #writerFile.writerow(["%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % name.childNodes[0].data], )
   writerFile.writerow((id, nome.childNodes[0].data, popularidade.childNodes[0].data, time.childNodes[0].data, genero.childNodes[0].data, altura.childNodes[0].data, peso.childNodes[0].data, localizacao.childNodes[0].data, inteligencia.childNodes[0].data, forca.childNodes[0].data, velocidade.childNodes[0].data, durabilidade.childNodes[0].data, energia.childNodes[0].data, Skils.childNodes[0].data))
   if time.childNodes[0].data == 'Bad':
      contBad = contBad+1;
      badFile.writerow((id, nome.childNodes[0].data, popularidade.childNodes[0].data, time.childNodes[0].data, genero.childNodes[0].data, altura.childNodes[0].data, peso.childNodes[0].data, localizacao.childNodes[0].data, inteligencia.childNodes[0].data, forca.childNodes[0].data, velocidade.childNodes[0].data, durabilidade.childNodes[0].data, energia.childNodes[0].data, Skils.childNodes[0].data))
      
   if time.childNodes[0].data == 'Good':
      contGood = contGood+1;
      goodFile.writerow((id, nome.childNodes[0].data, popularidade.childNodes[0].data, time.childNodes[0].data, genero.childNodes[0].data, altura.childNodes[0].data, peso.childNodes[0].data, localizacao.childNodes[0].data, inteligencia.childNodes[0].data, forca.childNodes[0].data, velocidade.childNodes[0].data, durabilidade.childNodes[0].data, energia.childNodes[0].data, Skils.childNodes[0].data))
      
   if nome.childNodes[0].data == "Hulk":
      imc = int (peso.childNodes[0].data) / int (altura.childNodes[0].data)**2


fileHerois.close()

# Print detail of each hero.
for hero in heroes:
#   if hero.hasAttribute("id"):
#     print ("Id: %s" % hero.getAttribute("id"))
   name = hero.getElementsByTagName('name')[0]
   print( "Id: {0} - {1}".format(hero.getAttribute("id"), name.childNodes[0].data))

#Duas formas de printar mais de um uma string na mesma linha: usando .format ou colocando entre "()"
print( "\nBom: %s - Ruim: %s" % (contGood, contBad) )
#5. Calcule, a partir dos dados do arquivo, e imprima na tela a proporção de heróis bons/maus.
print("Proporção de Herois bons: %.1f%%" % ((contGood*100)/cont))
print("Proporção de Herois maus: %.1f%%" % ((contBad*100)/cont))

#6. Calcule, a partir dos dados do arquivo, e imprima na tela a média de peso dos heróis
print("Peso medio: %.1f" % (contpeso/cont))

#7. Calcule, a partir dos dados do arquivo, e imprima na tela o "Índice de massa corporal” do Hulk
print("O IMC do Hulk é: ", imc )