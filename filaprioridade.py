# -*- coding: utf-8 -*-
#Fila estática
class FilaDePrioridade:
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
	def enqueue_with_priority(self, cidade_pai,cidade, custo):
		a = (cidade_pai,cidade, custo)
		self.dados.append(a)
		self.order_enqueue()

	#Ordena a fila com base no custo
	def order_enqueue():
		self.dados.sort(key=lambda x: x[2])

	def get_element(i):
		if i in range(0, len(self.dados)):
			return self.dados[i]

	#Remove na Fila (First out)
	def dequeue_priority(self):
		return self.dados.pop(0)

	#Imprime os elementos da estrutura
	def print_elem_priority(self):
		if self.dados!=None and self.dados!=[]:
			for e in self.dados:
				print(e, end = " ")
	
	#Verifica se a fila está vazia
	def isEmpty(self):
		if self.dados != None and self.dados!=[]:
			return False
		return True

	#Verifica se o elemento está na Fila
	def estaAqui(self, cidade):
		if self.isEmpty()==False:
			i = 0
			for e in self.dados:
				if valor == e[i][1]:
					return i;
				i+=1
		return False
