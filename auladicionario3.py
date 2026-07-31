alunos_info = ['mama','caca','atata']
ifspb = {'agro':['toto','zeze']}

ifspb['info'] = alunos_info

print(ifspb)

nome_curso = input('qual o nome do curso? ')
if nome_curso in ifspb:
    print(ifspb[nome_curso])