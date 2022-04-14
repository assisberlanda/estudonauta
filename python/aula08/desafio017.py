import math

print('==========  Desafio 017  ============')

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
h = math.hypot(co, ca)
print('A Hipotenusa vai medir {:.2f} '.format(h))
