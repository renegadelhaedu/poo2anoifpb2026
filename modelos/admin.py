class Admin:
    #construtor
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if len(novo_nome) == 0:
            print('nao pode atribuir nome vazio')
        else:
            self.nome = novo_nome
            print('modificado com sucesso')

    def trocar_senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.senha = nova_senha
            return True
        return False

    def verificar_login(self, login, senha):
        if login == self.nome and self.senha == senha:
            return True
        return False
