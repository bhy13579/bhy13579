n = int(input())
cnt = 'A'

for i in range(n):
    for _ in range(i + 1):
        print(cnt, end='')

        if cnt == 'Z':
            cnt = 'A'
        else:
            cnt = chr(ord(cnt) + 1)

    print()