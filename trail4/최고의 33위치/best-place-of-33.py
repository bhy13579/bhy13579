n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_coin = 0

# n x n 배열 가로 세로
for r in range(n-2):
    for c in range(n-2):
        total = 0
        # 3 x 3 배열
        for i in range(3):
            for j in range(3):
                total += arr[r+i][c+j]
            if max_coin < total:
                max_coin = total
print(max_coin)