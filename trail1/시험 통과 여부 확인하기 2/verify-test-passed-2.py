n = int(input())
count = 0

for i in range(n):
    score = list(map(int, input().split()))
    avg = sum(score) / 4

    if avg >= 60:
        print("pass")
        count += 1
    else:
        print("fail")

print(count)