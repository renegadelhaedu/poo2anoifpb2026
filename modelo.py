class CampusIFPB:
    #construtor
    def __init__(self, nome_cidade, diretor):
        #atributos da classe
        if nome_cidade == '' or diretor == '':
            print('voce atribuiu valores vazios')
        else:
            self.cidade = nome_cidade
            self.diretor = diretor
            self.cursos = []
            print('Campus criado com sucesso')

    #método da classe
    def criar_curso(self, nome_curso):
        if nome_curso in ['informatica','agropecuaria','agroindustria','meio ambiente']:
            self.cursos.append(nome_curso)
            print('curso criado com sucesso!')
        else:
            print('este curso nao pode ser criado')



