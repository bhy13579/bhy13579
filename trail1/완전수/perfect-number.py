start, end = map(int, input().split())

count = 0

for n in range(start, end + 1):
    sum_val = 0

    for i in range(1, n):
        if n % i == 0:
            sum_val += i

    if sum_val == n:
        count += 1

print(count)