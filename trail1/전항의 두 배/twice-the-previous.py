m, n = map(int, input().split())
arr = [m, n]

for i in range(8):
    num = (arr[-1]) + (2*arr[-2])
    arr.append(num)

print(*arr)


