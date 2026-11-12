n, t = map(int, input().split())
up = list(map(int, input().split()))
down = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    temp1 = up[n-1]
    temp2 = down[n-1]

    for i in range(n-1, 0, -1):
        up[i] = up[i-1]
        down[i] = down[i-1]

    up[0] = temp2
    down[0] = temp1

print(*up)
print(*down)