#desenvolva um algoritmo em python que leia o nome e a idade
#dos alunos do 2 ano e quando terminar exiba qual a média de idade
#lembre que a turma possui 28 alunos

soma = 0
#com 1 parametro
#range(quantidade de repetiçoes)
#range(6) 0,1,2,3,4,5

#com 2 parametros
#range(valor inicial, condiçao de parada)
#range(2,7) 2,3,4,5,6

#com 3 parametros
#range(valor inicial, condiçao de parada, incremento/decremento)
#range(3,10,2) 3,5,7,9



for i in range(28):
    nome = input('qual seu nome ')
    idade = int(input('qual sua idade '))
    soma = soma + idade

media = soma / 28

print(f'a media de idade desta turma foi {media} anos')
