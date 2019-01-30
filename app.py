# -*- coding: utf-8 -*-
from algoritmosDebusca import *

#Cria a Romenia Vazia
R = Romenia()

def main():
	criandoRomenia()
	
	info1 = input("Informe a origem: ")
	info2 = input("Informe o destino: ")
	'''resultado = teste(info1, info2)
	if(resultado!=True):
		print("Resultado não encontrado")
	else:
		print("De", info1, "a", info2, "tem custo", resultado)

	#Faz a busca em Profundidade
	print("Busca Em Profundidade")

	resultado = buscaEmProfundidade(info1, info2)
	if(resultado!= False):
		print("\tEncontrado:",resultado[1])
		print("\tCaminho Percorrido:", resultado[0])
	else:
		print("Não encontrado")
	'''
	caminho = buscaNoBFS(R, info1, info2)

	if (caminho==False):
		print("Erro na busca")
	else:
    	print("Menor caminho")
		print (caminho)
		print("Distância:", distanciaTotal(caminho))

def criandoRomenia():
	#Inserindo todas as informações sobre a Romênia
	R.insereCidades("Arad", ["Zerind", "Sibiu", "Timisoara"],[75,140,118])
	R.insereCidades("Zerind",["Arad","Oradea"],[75,71])
	R.insereCidades("Sibiu",["Arad", "Rimnicu Vilcea","Fagaras"],[140, 80,90])
	R.insereCidades("Timisoara",["Arad","Lugoj"],[118,111])
	R.insereCidades("Oradea",["Zerind","Sibiu"],[71,151])
	R.insereCidades("Lugoj",["Timisoara","Mehadia"],[111,70])
	R.insereCidades("Mehadia",["Lugoj","Drobeta"],[70,75])
	R.insereCidades("Drobeta",["Mehadia","Craiova"],[75,120])
	R.insereCidades("Craiova",["Pitesti", "Rimnicu Vilcea","Drobeta"],[138,146,120])
	R.insereCidades("Rimnicu Vilcea",["Pitesti", "Sibiu", "Craiova"],[97,80,146])
	R.insereCidades("Fagaras",['Sibiu','Bucareste'], [99,211])
	R.insereCidades("Pitesti",["Rimnicu Vilcea","Bucareste","Craiova"],[97,101,138])
	R.insereCidades("Bucareste",["Urziceni", "Pitesti","Giurgiu","Fagaras"],[85,101,90,211])
	R.insereCidades("Giurgiu",["Bucareste"],[90])
	R.insereCidades("Urziceni",["Bucareste", "Vaslui","Hirsova"],[85,142,98])
	R.insereCidades("Vaslui",["Iasi", "Urziceni"], [92,142])
	R.insereCidades("Hirsova",["Eforie", "Urziceni"],[86,98])
	R.insereCidades("Eforie",["Hirsova"],[86])
	R.insereCidades("Iasi",["Neamt", "Vaslui"],[87,92])
	R.insereCidades("Neamt",["Iasi"],[87])
	print("--------- MAPA -----------")
	print (R.cidades)
	print("--------- DISTÂNCIAS -----------")
	print (R.custo)

def distanciaTotal(caminho):
	distancia = 0
	for i in range(len(caminho) - 1):
		distancia += R.pegaCusto(caminho[i], caminho[i+1])
	return distancia
    	


main()
