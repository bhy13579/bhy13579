n = list(map(int, input().split()))

for i in range(1, 7):
    cnt = 0
    for num in n:
        if num == i:
            cnt += 1
    print(f"{i} - {cnt}")