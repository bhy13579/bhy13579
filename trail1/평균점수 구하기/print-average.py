score = list(map(float, input().split()))
sum_val = 0

for i in range(8):
    sum_val += score[i]

print(f"{sum_val/8:.1f}")