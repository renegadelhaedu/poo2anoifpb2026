from exemplo2905.disciplina import Disciplina
from exemplo2905.aluno import Aluno
from exemplo2905.professor import Professor

gustavo = Aluno('Gustavo', '293923')
clara = Aluno('Clara', '878787878')

adson = Professor('Adson', '1212121212')

alunos = [gustavo, clara]
aps = Disciplina('aps', adson, alunos)

raquel = Aluno('Raquel', '434342')
aps.add_aluno(raquel)

adson.nome = 'adson diego'

print(aps)