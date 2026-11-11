arr = [0] * 4

for i in range(3):
    symptom, temp = input().split()
    temp = int(temp)

    if symptom == 'Y' and temp >= 37:
        arr[0] += 1

    elif symptom == 'N' and temp >= 37:
        arr[1] += 1

    elif symptom == 'Y' and temp < 37:
        arr[2] += 1

    else:
        arr[3] += 1

print(*arr, end=' ')

if arr[0] >= 2:
    print('E')