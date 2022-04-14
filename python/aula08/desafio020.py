import random

print('==========  Desafio 019  ============')

n1 = str(input('Aluno 01: '))
n2 = str(input('Aluno 02: '))
n3 = str(input('Aluno 03: '))
n4 = str(input('Aluno 04: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentaçao é:\n{lista}')
