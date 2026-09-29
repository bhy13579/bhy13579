n = int(input())


for i in range(n):
    for j in range(i):       # 좌 공백    
        print('  ', end='')
    for j in range(n-i):
        print(n-i-j, end=' ')
    print()