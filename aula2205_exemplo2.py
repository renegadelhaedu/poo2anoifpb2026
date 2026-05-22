class Conta:
    def __init__(self, nome, salario, limite):
        self.__nome = nome
        self.__salario = salario
        self.__limite = limite

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario

us1 = Conta('jose', 20000, 5000)
print(us1.nome) #get
us1.nome = 'michael' #set
print(us1.nome)