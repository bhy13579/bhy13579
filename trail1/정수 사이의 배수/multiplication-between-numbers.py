a, b = map(int, input().split())
total = 0
count = 0


for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        total += i
        count += 1
avg = total / count
    
print(f"{total} {avg:.1f}")
