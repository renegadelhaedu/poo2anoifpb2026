from heranca.exemplo1_heranca import Aluno, Integrado

class Subse(Aluno):
    def __init__(self, nome, idade, matricula, periodo):
        super().__init__(nome,idade, matricula)
        self.periodo = periodo

    #sobreposição/sobrescrita de métodos
    def chamar_quadrilha(self):
        print('bora povo do subsequente, balança o quadril')


jr = Subse('junior', 20, 848482,'3p')
jr.chamar_quadrilha()

jc = Integrado('julio cesar',16,43534,'filosofia, historia')
jc.chamar_quadrilha()