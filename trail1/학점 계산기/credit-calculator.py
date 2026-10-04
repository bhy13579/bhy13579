n = int(input())
grade = list(map(float, input().split()))
sum_val = 0

for i in range(n):
    sum_val += grade[i]
average = sum_val / n
print(f"{average:.1f}")


if average >= 4.0:
    print("Perfect")
elif average >= 3.0:
    print("Good")
else:
    print("Poor")