#herança em POO (pilar)
#herança é a capacidade de classes herdarem métodos e atributos
#herança diminui o código verboso e melhor organiza a estrutura do programa

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def informar_fardamento(self):
        cor = input('Qual a cor da sua farda?')
        if cor == 'cinza':
            print('acho essa a mais bonita')
        elif cor == 'branca' or cor == 'verde':
            print('é bonitinha também')
        else:
            print('corre que vanessa vai te pegar e mandar para casa')

    def chamar_quadrilha(self):
        print('bora galera do ifpb, anarrie')

class Integrado(Aluno):
    def __init__(self, nome, idade, matricula, basicas):
        super().__init__(nome, idade, matricula)
        self.basicas = basicas

