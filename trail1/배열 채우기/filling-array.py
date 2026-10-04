a = list(map(int, input().split()))

for i in range(10):
    if a[i] == 0:
        a = a[:i]
        break

print(*a[::-1], end=' ')


# 중간에 0이 입력 되면 입력 종료
# if a[i] == 0: break