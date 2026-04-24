class Admin:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def trocar_senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.senha = nova_senha
            return True
        return False

    def verificar_login(self, login, senha):
        if login == self.nome and self.senha == senha:
            return True
        return False
