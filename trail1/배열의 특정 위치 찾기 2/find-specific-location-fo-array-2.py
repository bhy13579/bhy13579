a = list(map(int, input().split()))

odd_sum = 0
even_sum = 0

for i in range(10):
    if i % 2 == 0:
        odd_sum += a[i]
    else:
        even_sum += a[i]

print(abs(odd_sum - even_sum))