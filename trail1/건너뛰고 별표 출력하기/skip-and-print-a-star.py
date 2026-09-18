n = int(input())

for i in range(1, n):
    for j in range(i):
        print('*',end='')
    print('\n')

for i in range(n+1):
    for j in range(n-i):
        print('*', end='')
    print('\n')