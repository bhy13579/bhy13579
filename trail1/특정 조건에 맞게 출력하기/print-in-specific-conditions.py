n = list(map(int, input().split()))
arr = []


for i in n:
    if i == 0:
        break

    elif i % 2 == 0:
        arr.append(i//2)
    else:
        arr.append(i+3)
    
        
print(*arr)