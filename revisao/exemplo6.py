#criar um arquivo no modo a append no arquivo exisitente
arquivo = open('meusamores.txt','a')

pergunta = 'sim'
while pergunta == 'sim':
    nome = input('vá dizendo suas paixoes: ')
    arquivo.write(nome + '\n')
    pergunta = input('digite sim se voce tiver mais paixoes')

arquivo.close()