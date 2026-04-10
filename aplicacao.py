from modelo import CampusIFPB
campi = []

op = 99
while op != 0:
    print('----MENU de criaçao de campus----')
    print('1-criar campus')
    print('2-criar curso em um campus')
    print('3-listar todos os campi')

    op = int(input('qual opcao voce deseja: '))
    if op == 1:
        cidade = input('qual a cidade que será criada o campus? ')
        diretora = input('qual o nome da diretora ou diretor? ')
        novo_campus = CampusIFPB(cidade, diretora)
        campi.append(novo_campus)

    elif op == 3:
        print('\n------Lista de Campus-----')
        for campus in campi:
            print(f'Cidade:{campus.cidade} | Diretora:{campus.diretor} | Qtde cursos: {len(campus.cursos)}')
