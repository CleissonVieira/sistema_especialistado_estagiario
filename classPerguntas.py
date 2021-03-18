from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Computador liga?','computadorLiga'],
		['Alimentacao esta conectada', 'alimentacaoConectada'],	
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
