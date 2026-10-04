num = list(map(int, input().split()))
sum_val = 0
count = 0

for i in range(10):
    if num[i] == 0:
        break
    if num[i] % 2 == 0:
        sum_val += num[i]
        count += 1

print(f"{count} {sum_val}")