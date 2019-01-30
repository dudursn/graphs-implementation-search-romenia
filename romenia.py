# -*- coding: utf-8 -*-
class Romenia:
	'''Construtor da classe Romenia
	vizinhos: dicionario que contém os vizinhos da cidade
	custos: dicionario que contém as distâncias da cidade as suas vizinhas
	'''
	def __init__(self, vizinhos = {}, custos ={}):
		self.cidades = vizinhos
		self.custo = custos	

	'''
	Insere os vizinhos e as distâncias da cidade atual
	key : cidade atual
	vizinhos: dicionario que contém os vizinhos da cidade(key do dict)
	custos: dicionario que contém as distâncias da cidade(key do dict) as suas vizinhas
	'''
	def insereCidades(self, key, vizinhos = [], custos = []):
		if self.cidades!=None:
			if key in self.cidades:
				if (all(vizinhos)):
					for i in range(0,len(vizinhos)):
						self.cidades[key].append(vizinhos[i])
						self.custo[key].append(custos[i])
				else:
					self.cidades[key].append(vizinhos)
					self.custo[key].append(custos)
			else:
				self.cidades[key] = vizinhos
				self.custo[key] = custos
				
	'''
	Retorna a posição do vizinho no dicionario se existir, caso não retorna False
	'''
	def indexPos(self, origem, vizinho):
		try:
			return self.cidades[origem].index(vizinho)
		except ValueError:
			return False

	'''
	Retorna a distancia de uma cidade a outra
	'''
	def pegaCusto(self, origem, vizinho):
		if origem in self.cidades:
			try:
				if self.cidades[origem].index(vizinho):
					a = self.indexPos(origem, vizinho)
					return self.custo[origem][a]
			except ValueError:
				return False
		return False

	def numVizinhos(self, origem):
		return len(self.cidades[origem])
	'''
	Retorna os vizinhos e as distâcias da cidade atual
	'''
	def pegaVizinhos(self, cidade):
		lista = []
		for i in range(0, len(self.cidades[cidade])):
			lista.append((self.cidades[cidade][i],self.custo[cidade][i]))
		return lista

	#Verifica se existe essa cidade na Romenia
	def verificaCidade(self, cidade):
		for keys in self.cidades:
			if keys == cidade:
				return True
		return False

