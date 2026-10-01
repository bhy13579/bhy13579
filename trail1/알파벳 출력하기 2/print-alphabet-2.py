n = int(input())
cnt = 'A'

for i in range(n):
    for j in range(i):
        print('  ', end='')

    for j in range(n-i):
        print(cnt, end=' ')

        if cnt == 'Z':
            cnt = 'A'
        else:
            cnt = chr(ord(cnt) + 1)

    print()