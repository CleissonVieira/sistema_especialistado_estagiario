from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
pergunta = Pergunta()

proxPergunta = 'computador_liga'

while proxPergunta != 'Fim':
	string = pergunta.texto(proxPergunta)
	proxPergunta = se.pergunta(string[0],string[1])


print(string[1])


