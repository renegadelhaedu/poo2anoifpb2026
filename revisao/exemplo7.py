#criar um arquivo no modo a append no arquivo exisitente
arquivo = open('crushs.txt','a')

pergunta = 'sim'
while pergunta == 'sim':
    nome = input('qual o nome? ')
    nota = input('quao impactante essa pessoa foi? ')
    arquivo.write(nome + '-' + nota + '\n')
    pergunta = input('digite sim se voce tiver mais paixoes')

arquivo.close()