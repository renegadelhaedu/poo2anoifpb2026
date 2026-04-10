class Aluno:
    #construtor da classe
    #serve para criar objetos da classe
    def __init__(self, nome, sua_matricula):
        self.nome = nome
        self.matricula = sua_matricula

#criar/instanciar um objeto
davi = Aluno('davi gabriel', 42652348675)
raquel = Aluno('Ana Raquel', 984957355)
print(davi.nome)
print(raquel.nome)
