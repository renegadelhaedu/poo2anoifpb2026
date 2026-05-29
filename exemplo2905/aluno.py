class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def __repr__(self):
        return f'Nome:{self.nome} | Mat:{self.matricula}'