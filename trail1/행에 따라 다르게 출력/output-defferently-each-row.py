n = int(input())
cnt = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(1, n+1):
            cnt += 1
            print(cnt, end=' ')
    else:
        for j in range(1, n+1):
            cnt += 2
            print(cnt, end=' ')
    print()