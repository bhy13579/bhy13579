n, t = map(int, input().split())

left = list(map(int, input().split()))
right = list(map(int, input().split()))
down = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    temp1 = left[n-1]
    temp2 = right[n-1]
    temp3 = down[n-1]

    for i in range(n-1,0,-1):
        left[i] = left[i-1]
        right[i] = right[i-1]
        down[i] = down[i-1]
    left[0] = temp3
    right[0] = temp1
    down[0] = temp2

print(*left)
print(*right)
print(*down)   