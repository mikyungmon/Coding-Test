a, b = map(int, input().strip().split(' '))
for i in range(b):   # 세로
    for j in range(a):  # 가로
        print('*', end='')  # end='' -> 개행 제거하는거

    print('')