# -*- coding: utf-8 -*-
#Pilha estática
class Pilha:
	#Construtor da classe Fila
	def __init__(self):
		self.dados = []
	
	#Retorna o numero de elementos	
	def numElem(self):
		return len(self.dados)

	#Retorna quem está no topo
	def top(self):
		return self.dados[len(self.dados)-1]

	#Insere no topo (First in)
	def pushP(self, valor):
		self.dados.append(valor)

	#Remove no topo Pilha (Last out)
	def popP(self):
		return self.dados.pop()

	#Verifica se o elemento está na Pilha
	def estaAqui(self, valor):
		if self.dados!=None:
			if valor in self.dados:
				return True
		return False

	#Verifica se a Pilha esta vazia
	def estaVazia(self):
		if self.dados ==[]:
			return True
		return False

	#Imprime os elementos da estrutura
	def printElem(self):
		if self.dados!=None and self.dados!=[]:
			for e in self.dados:
				print(e, end = " ")

	#Verifica se a pilha está vazia
	def isEmpty(self):
		if self.dados != None and self.dados!=[]:
			return True
		return False