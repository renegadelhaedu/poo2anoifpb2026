def verificar_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

novo_email = input('informe seu e-mail: ')

saida = verificar_email(novo_email)
print(saida)