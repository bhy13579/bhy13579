N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        space = i - 1
        star = 2 * (N - i) + 1
    else:
        space = 2 * N - i - 1
        star = 2 * (i - N) + 1

    print("  " * space + "* " * star)