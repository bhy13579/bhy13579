n = list(map(int, input().split()))

for i in range(100, 0, -10):
    cnt = 0

    for num in n:
        if num == 0:
            break
        if (num // 10) * 10 == i:
            cnt += 1
    print(f"{i} - {cnt}")