#tabuada


while True:
    n = int(input('Quer ver a Tabuada de qual número? '))
    print('=' * 13)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('=' * 13)
print('VOLTE SEMPRE!')