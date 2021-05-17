#o objetivo desse Algoritmo é organizar pastas de acordo com o tipo de arquivo.


import os

#listas com as possíveis extensões:
extensoes = {'audios': ['MP3', 'WAV', 'WMA', 'AAC'],
	     'imagens': ['JPG', 'PNG', 'JPEG'],
	     'videos': ['MP4', 'AVI', 'FLV'],
	     'documentos': ['DOC', 'DOCX', 'TXT', 'PDF'],
	     'outros': []}
path_type_file = {}


#ler a extensão de um arquivo:
def extensao(nome):
	p = nome.rfind('.')
	extensao = nome[p+1:]
	return extensao

#pegar o nome dos arquivos:
def organizando(diretorio):

	lista_arquivos = os.listdir(diretorio)
	#criar o caminho da pasta de cada tipo de arquivo (áudios, imagens...)
	for key in extensoes.keys():
		path = os.path.join(diretorio, key)
		path_type_file[key] = path

	#evitar problemas de criar pastas existentes 
	#criada na primeira vez em que executamos o código.
	for path in path_type_file.values():
		if not os.path.isdir(path):
			os.mkdir(path)

	for arq in lista_arquivos:
		if os.path.isfile(os.path.join(diretorio, arq)):
			#Lê e retorna a extensão do arquivo.
			ext_arq = extensao(str(arq.upper()))
			#compara a extensão lida com as extensões disponíveis no dicionário 'extensoes' e depois move o arquivo.
			for key, ext in extensoes.items():
				if ext_arq in ext or key == 'outros':
					os.rename(os.path.join(diretorio, arq), os.path.join(path_type_file[key], arq))
					break


	
if __name__ == '__main__':
	organizando(os.path.abspath('download'))
