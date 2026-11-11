n = int(input())
m = list(map(int, input().split()))

arr = [0] * 10

for i in m:
    arr[i] += 1

for i in range(1, 10):
    print(arr[i])