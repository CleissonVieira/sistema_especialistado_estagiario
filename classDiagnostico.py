class Diagnostico():
	# metodo construtor
	def __init__(self):
		self.pessoa = []
		self.db = []
		# abre o arquivo db.txt em modo leitura e passa os dados para
		# uma lista de listas de str
		arquivo = open('db.txt','r')
		for linha in arquivo:
			if linha[len(linha) - 1] == '\n':
				linha = linha.replace("\n", "")
				(self.db).append(linha.split('-'))
		arquivo.close()

	# imprime a quantidade de possibilidades cadastradas
	def tamanho(self):
		print(len(self.resultado))
	
	def buscaDb(self, resposta, caract):	
		for i in range(len(self.db)):
			if caract == self.db[i][0]:
				if self.db[i][1] == resposta:
					return self.db[i][2]
		return 'Fim'

	def proxPergunta(self, resposta, caract):
		pergunta = self.buscaDb(resposta, caract)	
		return pergunta
		
	def pergunta(self,caract, pergunta):
		if self.proxPergunta('sim', caract) == 'Fim':
			return 'Fim'
	
		resp = input(pergunta)
		if resp == 'sim' or resp == 'Sim':
			return self.proxPergunta('sim', caract)
		elif resp == 'nao' or resp == 'Nao':
			return self.proxPergunta('nao', caract)
