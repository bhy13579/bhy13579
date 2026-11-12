n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 1
happy = 0

# 가로열 순회
for i in range(n):
    cnt = 1    
    if cnt >= m:
        happy += 1
        continue
       
 
    for j in range(1, n):
        if arr[i][j] == arr[i][j-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            happy += 1
            break

# 세로?
for j in range(n):
    cnt = 1    
    if cnt >= m:
        happy += 1
        continue
    
    for i in range(1, n):
        if arr[i][j] == arr[i-1][j]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            happy += 1
            break

    

print(f"{happy}")