def verificar_davis(lista):
    qtde = 0
    for nome in lista:
        if 'davi' in nome.lower():
            qtde += 1

    return qtde

alunos = ['francisca','davi gabriel','lucas','Davi lyan','eduarda']

print(verificar_davis(alunos))