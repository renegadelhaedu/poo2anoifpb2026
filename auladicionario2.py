alunos_info = ['mama','caca','atata']
ifspb = {'agro':['toto','zeze']}

ifspb['info'] = alunos_info

print(ifspb)

#remover par -> pop remove pela chave

if 'meio' in ifspb:
    ifspb.pop('meio')
else:
    print('nao existe')