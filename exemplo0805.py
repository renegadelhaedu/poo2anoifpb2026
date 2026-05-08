from modelos.admin import Admin

repre = Admin('eduarda sousa', '123456')

'''nao faço mais isso
print(repre.nome)
repre.nome = 'maria eduarda sousa'
'''

#agora eu faço isso
print(repre.get_nome())
repre.set_nome('maria eduarda sousa')
print(repre.get_nome())