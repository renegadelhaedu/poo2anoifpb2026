class Rene():
    def __init__(self, nome):
        self.valor = 123.123
        self._salario = 1
        self.__nome = nome
    def mostrar_salario(self):
        print(self._salario)
    def mudar_nome(self, novo_nome):
        self.__nome = novo_nome
        print(self.__nome)


#aqui eu estou instanciando um objeto da classe Rene
a = Rene("a")

#a.__nome = "b"
a.mudar_nome("b")

#pythonic

