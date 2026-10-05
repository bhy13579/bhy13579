a = list(map(int, input().split()))

sum_even = 0
sum_three = 0
count = 0

for i in range(10):
    if (i + 1) % 2 == 0:
        sum_even += a[i]

    if (i + 1) % 3 == 0:
        sum_three += a[i]
        count += 1

avg = sum_three / count

print(f"{sum_even} {avg:.1f}")