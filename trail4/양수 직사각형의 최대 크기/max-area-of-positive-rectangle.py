n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        for i2 in range(i, n):
            for j2 in range(j, m):
                cnt = 0
                for r in range(i, i2+1):
                    for c in range(j, j2+1):
                        if arr[r][c] <= 0:
                            cnt += 1

                if cnt == 0:
                    
                    asdf = (i2+1-i)*(j2+1-j)
                    if asdf >= ans:
                        ans = asdf
if ans == 0:
    print(-1)
else:
    print(ans)
