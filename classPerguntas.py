from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['computador_liga', 'Computador liga?'],
		['fonte_inicia', 'A fonte inicia?'],
		['alimentacao_conectada', 'A alimentacao está conectada?'],
		['voltagens_corretas', 'A voltagem está correta?'],
		['a_bios_esta_iniciando', 'A BIOS está iniciando ?'],
		['speaker_emite_alertas', 'O speaker emite alertas?'],
		['boot_os', 'Boot OS?'],
		['unidade_de_armazenamento_detectada', 'A unidade de armazenamento é detectada?'],
		['ordem_de_boot_correta', 'A ordem de boot está correta?'],	
		['unidade_de_armazenamento_integra', 'A unidade de armazenamento está integra?'],
		['os_inicia_completamente', 'OS inicia completamente?'],
		['funcionamento_normal', 'Fique feliz, porque seu computador está funcionando perfeitamente! :)'],
		['problema_na_placa_mae', 'Deu ruim, deu problema na placa mae. Procure uma assistência técnica.'],
		['checar_processador_e_memoria_ram', 'Deu ruim, problema no processador ou memória ram. Troque a pasta térmica e passe borracha na memória ram.'],
		['fonte_queimada', 'Você deu sorte, a fonte está queimada e não a placa de vídeo. Fonte é bem mais barata.'],
		['conectar_alimentacao', 'Pelas suas respostas, é só ligar o pc na tomada. Ainda não existe energia Wi-Fi.'],
		['fonte_com_problema', 'Alguma coisa não está certa com sua fonte. Leve pro Renan.'],
		['checar_circuito_de_alimentacao', 'Bah, deu problema no circuito de alimentação da placa mãe. Leve para a assistência.'],
		['hd_ou_ssd_desconectado_ou_com_defeito', 'O HD/SSD não está conectado. Se estiver conectado, o HD/SSD está com defeito. Dessa forma, é necessário fazer a troca.'],
		['ajustar_boot', 'Bem lógico isso, não preciso nem responder né.'],
		['substituir_hd_ou_ssd', 'Troque o HD/SDD.'],
		['imagem_so_corrompida', 'O Sistema Operacional está corrompido. Faça o reparado dos arquivos do sistema. Se der certo, ótimo. Caso contrário, faça a reinstalação do Sistema Operacional.']
		]

	def texto(self, pergunta):
		for i in range(len(self.level)): 
			if self.level[i][0] == pergunta:
				return self.level[i]
