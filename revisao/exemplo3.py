professor_a = []

nome = input('digite o nome de uma namorada(o) sua ou fim caso tenha terminado')

while nome != 'fim':
    professor_a.append(nome)
    nome = input('digite o nome de uma namorada(o) sua ou fim caso tenha terminado')

qtde = len(professor_a)
print(f'voce teve ao longo da vida {qtde} namoradas(os)')

if qtde > 0:
    print('a ultima pessoa foi', professor_a[-1])

#faça um for para mostrar a lista de nomes
for ex in professor_a:
    print(ex)

for i in range(len(professor_a)):
    print(professor_a[i])



