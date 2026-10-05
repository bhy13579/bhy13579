start, end = map(int, input().split())

answer = 0

for n in range(start, end + 1):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 3:
        answer += 1

print(answer)