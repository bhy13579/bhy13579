cnt = 0

for _ in range(3):
    symptom, temp = input().split()
    temp = float(temp)

    if symptom == 'Y' and temp >= 37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')