a, b = map(int, input().split())

arr = [0] * b

while a > 1:
    r = a % b
    arr[r] += 1
    a = a // b

total = 0

for i in arr:
    total += i ** 2

print(total)