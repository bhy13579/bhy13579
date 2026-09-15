
total = 0
count = 0


for i in range(10):
    T = (int(input()))
    if T >= 0 and T <= 200:
        total += T
        count += 1
avg = total / count
    
print(f"{total} {avg:.1f}")


