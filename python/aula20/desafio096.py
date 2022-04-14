def area(a, b):
    print('-=' * 5, f'{"ÁREA DO TERRENO":^30}', '-=' * 5)
    print()
    area = a * b
    print(f'A área do terreno de {a} X {b} é {area}.')
    print()
    print('-=' * 5, f'{"OBRIGADO":^30}', '-=' * 5)


l = int(input('Qual a largura do terreno em (m): '))
c = int(input('Qual o comprimento do terreno em (m): '))
area(l, c)
