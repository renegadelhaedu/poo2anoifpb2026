#revisar lista
#estrutura de dados que os itens estão ordenados sequencialmente
alunos = ['rene','maria','pedro']


#dicionário
#é outra estrutura de dados que os valores são representados
#por pares -> chave:valor
#nos valores, você pode colocar qualquer tipo de dado (lista, dict..)
#as chaves sejam únicas, valores podem se repetir
profs = {2342:'rene' , 3341:'guga', 9876:'adson'}
profs2 = {2342:['rene', 30] , 4753:['guga', 27], 9876:['adson', 93]}

#print(profs2[4753][1])
#colocar a chave entre colchetes é a forma de chamar um valor específico
#print(profs[2342])

#adicionando um par ao dicionário
profs[6211] = 'jefferson'
print(profs)

#alterar valores
for i in range(2):
    print(profs)
    mat = int(input('qual a matricula do prof para alterar? '))
    novo_nome = input('Qual o novo nome do prof? ')
    if mat in profs:
        profs[mat] = novo_nome
        print(profs)
    else:
        print('sinto muito, nao achamos essa criatura')