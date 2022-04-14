import math
print('==========  Desafio 018  ============')
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O Ângulo de {:.2f} tem o Seno de {:.2f}\nO Cosseno de {:.2f}\n e a Tangente de {:.2f}'.format(ang, sen, cos, tan))
