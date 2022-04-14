matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a matriz na posiçao [{l}, {c}]: '))
print('=' * 20)
print(f'{"MATRIZ 3 X 3":^20}')
print('=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 20)