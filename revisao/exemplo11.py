def niver_bele(convidados):
    filtrados = []
    for pessoa in convidados:
        if pessoa[1] >= 50:
            filtrados.append(pessoa[0])
    return filtrados

lista = []

pergunta = 'sim'
while pergunta != 'nao':
    nome = input('qual teu nome? ')
    valor = float(input('quanto voce vai presentear? '))
    lista.append([nome, valor])
    pergunta = input('quer continuar?')

saida = niver_bele(lista)
#len é uma funçao que diz quantos elementos a lista possui
if len(saida) > 0:
    for confirmado in saida:
        print(f'oi {confirmado},voce nao foi mao de vaca e vai pro niver')
else:
    print('só tem mao de vaca')