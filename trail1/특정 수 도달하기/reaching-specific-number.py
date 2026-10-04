a = list(map(int, input().split()))

for i in range(10):
    if a[i] >= 250:
        a = a[:i]
        break

print(f"{sum(a)} {(sum(a)/len(a)):.1f}", end=' ' )