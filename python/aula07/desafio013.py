print('==========  Desafio 013  ============')
n = str(input('Qual é seu nome? '))
c = str(input('Qual é o seu cargo atualmente? '))
s = int(input(f'Qual o seu salário no cargo de {c}? R$'))
a = float(input('Quantos % de aumento você gostaria de receber? %'))
ns = s+(s*a)/100
print('Parabéns {}, você acaba de ser promovido à Gerende de {}, e receberá um aumento de {}%,\n e o seu novo salário será R${:.2f}'.format(n,c,a,ns))
print('\n\nIsso não é Maravilhoso!!!')