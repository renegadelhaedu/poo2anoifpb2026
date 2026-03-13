#desenvolva um algoritmo em python que leia o nome e a idade
#dos alunos do 2 ano e quando terminar exiba qual
# a média de idade, a menor idade, a maior idade e
# o nome do penultimo aluno que digitou
#lembre que a turma possui 28 alunos

soma = 0
menor = 100
maior = 0
for i in range(28):
    nome = input('qual seu nome ')
    idade = int(input('qual sua idade '))
    soma = soma + idade

    if idade < menor:
        menor = idade

    if idade > maior:
        maior = idade

    if i == 26:
        print(nome, idade)

media = soma / 28

print(f'a media de idade desta turma foi {media} anos')
