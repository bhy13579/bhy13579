num = list(map(int, input().split()))
sum_val = 0
count = 0

for i in range(10):
    if num[i] == 0:
        break
    sum_val += num[i]
    count += 1

print(f"{sum_val} {sum_val/count:.1f}")