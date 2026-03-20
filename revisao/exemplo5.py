#criar um arquivo no modo w reseta tudo que tem dentro dele
arquivo = open('meusamores.txt','w')

pergunta = 'sim'
while pergunta == 'sim':
    nome = input('vá dizendo suas paixoes: ')
    arquivo.write(nome + '\n')
    pergunta = input('digite sim se voce tiver mais paixoes')

arquivo.close()