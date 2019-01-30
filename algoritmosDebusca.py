# -*- coding: utf-8 -*-
from romenia import Romenia
from fila import Fila
from pilha import Pilha
from filaprioridade import FilaDePrioridade

############################
#	BUSCA EM PROFUNDIDADE  #
############################
'''
Faz a busca em profundidade com auxilio da função recursiva buscaNo
origem: cidade de partida
destino: cidade de destino
retorna False se as cidades nao existem
ou retorna q foi encontrado e o caminho percorrido até chegar o resultado
'''
def buscaEmProfundidade(R, origem, destino):
	#Armazena os dados que ja apareceram pelo menos uma vez e após serem expandidos são removidos
	Borda = Pilha()
	#Os nós removidos(que foram totalmente explorados) da pilha são armazendados na fila
	Explorado = Fila()
	#Guarda o caminho percorrido até chegar o lugar
	caminho = []
	#No auxiliar
	no = []
	#Testa se as cidades em pesquisa existem
	if(R.verificaCidade(origem)!=True or R.verificaCidade(origem)!=True):
		return False

	#Colocando valores no estado inicial
	no = R.cidades[origem]
	Borda.pushP(origem)	
	resultado = buscaNoDFS(R,no, origem, destino, Explorado, caminho, Borda)


	return caminho,resultado

'''
buscaNo: função recursiva que retorna o resultado da busca
no: cidades vizinhas a cidade atual
atual: cidade atual onde está a busca
caminho: lista do caminho percorrido
Borda: É uma pilha que armazena as cidades que da não foram explorados, mas que foram visitados, após não existir mais expansão a cidade é removida
Explorados: cidades que saem da Borda são armazenados na Fila
'''
def buscaNoDFS(R, no, atual, destino, Explorado, caminho, Borda):

	caminho.append(atual)
	#Se foi encontrado
	if (destino==atual):
		return True
	#Percorre os vizinhos da cidade atual
	else:
		i = 0
		while(i<len(no)):
			#Caso cidade atual ainda não foi explorada
			atual = no[i]

			i = i+1
			print(Borda.dados)
			if(Explorado.estaAqui(atual)):
				pass
			else:
				if(not Borda.estaAqui(atual)):
					Borda.pushP(atual)	
						
					no = R.cidades[atual]
					#Busca-se novos vizinhos para a cidade atual
					if(buscaNoDFS(R,no, atual, destino, Explorado, caminho, Borda)==True):
						return True

		Explorado.enqueue(Borda.popP())

		return False		
			
############################
#	BUSCA EM LARGURA       #
############################
'''
Borda: cidades visitadas
Explorado: cidades expandidas
caminho = 0:cidade_pai, 1: cidade_filha
no: lista de cidades vizinhas a cidade atual
'''
def buscaNoBFS(R, origem, destino):
	#Inicia as filas Borda e o Explorado vazios
	Borda = Fila()
	Explorado = Fila()
	#Guarda todos os lugares e os anteriores para chegar a esse lugar
	caminho = []
	#Coloca a origem na borda
	Borda.enqueue(origem)
	#A origem não tem lugar anterior a ele
	caminho.append((' ',origem))
	#Teste de objetivo
	if (destino==origem):
		return caminho
	
	while(Borda.isEmpty()!=True):
		atual = Borda.dequeue()
		Explorado.enqueue(atual)
		no = R.cidades[atual]
		for i in range(0,len(no)):
			filho = no[i]
			if Explorado.estaAqui(filho)==False and Borda.estaAqui(filho)==False:
				Borda.enqueue(filho)
				caminho.append((atual,filho))
				#Teste de objetivo com os filhos
				if filho == destino:
					return pegaCaminhoFinalBFS(caminho)

	return False
	
#Função auxiliar da BFS, retorna o caminho final, ou seja, o que passa por menos vértices
def pegaCaminhoFinalBFS(caminho):
	caminhoFinal = []
	#Insere o destino 
	caminhoFinal.append(caminho[-1][1])
	#Pega por onde veio para chegar no destino
	atual = caminho[-1][0]
	#Enquanto não existir o pai, que no caso seria a origem
	while(atual != ' '):
		#Insere o lugar atual no caminho final
		caminhoFinal.append(atual)
		#Procura o caminho anterior(chamado pai) para chegar no lugar atual
		pai = procuraPaiBFS(atual, caminho)
		#O lugar anterior será o novo atual
		atual = pai
		
	caminhoFinal.reverse()
	return caminhoFinal

#Função auxiliar da BFS, procura o caminho anterior para chegar no lugar atual
def procuraPaiBFS(lugar, caminho):
	for i in range(0,len(caminho)):
		if(lugar==caminho[i][1]):
			return caminho[i][0]
	return None


############################
#	BUSCA CUSTO UNIFORME   #
############################

'''
Borda = 0:cidade_pai, 1: cidade_atual, 2: custo
Explorado = cidades expandidas
'''
def buscaCustoUniforme(R, origem, destino):
	#Inicia as filas Borda e o Explorado vazios
	Borda = enqueue_with_priority()
	Explorado = Fila()
	#Guarda todos os lugares e os anteriores para chegar a esse lugar
	caminho = []
	#Coloca a origem na borda
	Borda.enqueue((' ',origem, 0))
	#A origem não tem lugar anterior a ele e custo 0
	caminho.append((' ',origem, 0))
	
	while(Borda.isEmpty()!=True):
		atual = Borda.dequeue()
		#Atual[1] é a cidade que será expandida no momento
		no = R.cidades[atual[1]]
		#Teste de objetivo com a cidade atual
		if atual[1] == destino:
			return caminho
		Explorado.enqueue(atual[1])

		for i in range(0,len(no)):
			filho = no[i]
			if Explorado.estaAqui(filho)==False and Borda.estaAqui(filho)==False:
				#custo = pegaCusto(atual[1], filho)
				Borda.enqueue(filho)
			else:
				caminho.append((atual,filho))
				

	return False


#Pega o custo de uma cidade a outra
def pegaCusto(R, origem, vizinho):
	return (R.pegaCusto(origem, vizinho))

def pegaCustodoPaiaoFilho(lugar, caminho):
	for i in range(0,len(caminho)):
		if(lugar==caminho[i][1]):
			return caminho[i][0]
	return None