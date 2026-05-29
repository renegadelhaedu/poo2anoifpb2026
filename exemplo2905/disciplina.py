from exemplo2905.aluno import Aluno
from exemplo2905.professor import Professor

class Disciplina:
    def __init__(self, nome_disciplina, professor, lista_alunos):
        self.nome_discplina = nome_disciplina
        self.professor = professor
        self.lista_alunos = lista_alunos

    def add_aluno(self, aluno):
        self.lista_alunos.append(aluno)

    def __repr__(self):
        return f'{self.nome_discplina} | {self.professor}'