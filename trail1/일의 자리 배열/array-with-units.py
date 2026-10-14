a, b = map(int, input().split())
arr = [a, b]

for i in range(2, 10):
    num = (arr[i-2] + arr[i-1]) % 10

    arr.append(num)

print(*arr)