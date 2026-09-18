n = int(input())

for count in range(2):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()

    if count == 0:
        print() 