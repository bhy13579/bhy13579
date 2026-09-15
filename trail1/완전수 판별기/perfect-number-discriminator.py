n = int(input())
perfect_number = 0

for i in range(1,n):
    if n % i == 0:
        perfect_number += i

if perfect_number == n:
    print('P')
else:
    print('N')
