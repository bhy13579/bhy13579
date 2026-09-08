n = int(input())

if n % 2 == 1:
    if n < 9:
        print(31)
    else:
        print(30)
elif n % 2 == 0:
    if n >= 8:
        print(31)
    elif n == 2:
        print(28)
    else:
        print(30)
