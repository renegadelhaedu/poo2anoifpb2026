class Professor:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    #encapsulamento: var privadas -> métodos de acesso públicos
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #ensina ao print como exibir um objeto desta classe na tela
    def __repr__(self):
        return f'Prof {self.nome}'