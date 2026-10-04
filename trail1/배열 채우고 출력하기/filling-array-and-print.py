arr = list(map(str, input().split()))

arr.reverse()
for i in range(10):
    print(arr[i], end='')