n = int(input())
arr = [1, n]

while True:
    num = arr[-2] + arr[-1]
    arr.append(num)
    if num > 100:
        break
print(*arr)