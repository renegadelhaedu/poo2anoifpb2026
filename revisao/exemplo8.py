#ler o arquivo no modo r
arquivo = open('crushs.txt','r')
#converte o texto em linhas e joga dentro de uma lista
linhas = arquivo.readlines()
arquivo.close()

soma = 0
for linha in linhas:
    #split é uma funcao que divide a string de acordo com o caractere informado
    nome = linha.split('-')[0]
    nota = linha.split('-')[1]
    soma = soma + float(nota)

media = soma / len(linhas)
print(media)

