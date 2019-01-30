# -*- coding: utf-8 -*-
#Fila estática
class Fila:
	#Construtor da classe Fila
	def __init__(self):
		self.dados = []

	#Retorna o primeiro da fila
	def first(self):
		return self.dados[0]

	#Retorna o último da fila
	def last(self):
		return self.dados[len(self.dados)-1]

	#Insere na Fila (First in)
	def enqueue(self, valor):
		self.dados.append(valor)

	#Remove na Fila (First out)
	def dequeue(self):
		return self.dados.pop(0)

	#Imprime os elementos da estrutura
	def printElem(self):
		if self.dados!=None and self.dados!=[]:
			for e in self.dados:
				print(e, end = " ")
	
	#Verifica se a fila está vazia
	def isEmpty(self):
		if self.dados != None and self.dados!=[]:
			return False
		return True

	#Verifica se o elemento está na Fila
	def estaAqui(self, valor):
		if self.dados!=None:
			if valor in self.dados:
				return True
		return False
