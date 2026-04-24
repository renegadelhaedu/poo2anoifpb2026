#como importar:
#está dentro de uma pasta?
#from nome_da_pasta.arquivo import Classe

#nao está dentro de pasta/pacote
#from nome_arquivo import Classe
from modelos.admin import Admin
alunos = []

alunos.append(Admin('rafael', 'estouamando'))
alunos.append(Admin('maria', 'souaamada'))
alunos.append(Admin('carol', 'traida'))

login = input('digite seu login')
senha = input('digite sua senha')

usuario_logado = None
for aluno in alunos:
    if aluno.verificar_login(login, senha):
        usuario_logado = aluno

if usuario_logado:
    #entra aqui se usuario_logado tiver um objeto dentro
    op1= 99
    while op1 != 0:
        print('menu aluno')
        print('1-trocar senha')
        op1 = int(input('digite sua opcao'))
        if op1 == 1:
            nova_senha = input('digite sua nova senha')
            if usuario_logado.trocar_senha(nova_senha):
                print('senha trocada com sucesso')
            else:
                print('sua senha deve conter pelo menos 8 caracteres')
        elif op1 == 2:
            print(usuario_logado.nome)
            print(usuario_logado.senha)
else:
    print('login ou senha incorreto')